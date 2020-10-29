from django.utils import timezone

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as log_out
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


from mrrobot_scavenger_hunt.apps.game.models import Game, GameStep, Path, Log


@csrf_exempt
def index(request):
    context = {
        'mode': 'attack'
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context.update({
                'game_in_progress': False
            })
        else:
            context.update({
                'message': 'Invalid Credentials. Please try again',
            })

    set_timer(request, context)
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def set_timer(request, context):
    if request.user.is_authenticated and not request.user.is_staff:
        try:
            game = Game.objects.get(user=request.user)
            current_time = timezone.now()
            diff = current_time - game.start_date
            ms = diff.seconds * 1000
            context["timer_ms"] = ms
        except Game.DoesNotExist:
            pass


@csrf_exempt
def signup(request):
    context = {
        'page_title': 'Sign Up',
        'mode': 'attack'
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
            context['message'] = "This username already exists"
        except User.DoesNotExist:
            if username and password:
                user = User.objects.create(username=username)
                user.set_password(password)
                user.save()
                return redirect('index')
            else:
                context['message'] = "Please fill all the fields"
    else:
        context['message'] = 'Please enter your information'

    template = loader.get_template('signup.html')

    return HttpResponse(template.render(context, request))


def logout(request):
    log_out(request)
    template = loader.get_template('logout.html')
    return HttpResponse(template.render({}, request))


@login_required(login_url='/')
@staff_member_required
def start_game(request):
    games = Game.objects.filter(status=Game.IN_PROGRESS)
    already_started = False
    if games.exists():
        already_started = True
        message = "There's a game in progress"
    else:
        users = User.objects.exclude(is_staff=True)
        paths = Path.objects.all()

        if users.count() <= paths.count():
            counter = 0
            for user in users:
                game, _ = Game.objects.get_or_create(user=user,
                                                     path=paths[counter],
                                                     status=Game.IN_PROGRESS)
                game.start()
                counter+=1
            message = "Game Started!!"
        else:
            message = "Hay mas jugadores que path, configurelo por admin"

    template = loader.get_template('index.html')
    return HttpResponse(template.render({'message': message,
                                         'already_started': already_started,
                                         'page_title': 'Start Game',
                                         'mode': 'attack'
                                         },
                                         request))


@login_required
def game(request):
    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        game_step = game.current_step
        if request.method == 'POST' and 'puzzle_answer' in request.POST:
            puzzle_answer = request.POST.get('puzzle_answer')
            if game_step.step.puzzle.answer.lower() == puzzle_answer.lower():
                game_step.is_puzzle_solved = True
                game_step.save()
        context = {'game': game,
                   'page_title': game.mode.upper() if not game.on_mission else 'mission',
                   'mode': game.mode.lower() if not game.on_mission else 'mission'
                 }
    except Game.DoesNotExist:
        return redirect('index')

    if game.score == game.gamestep_set.count():
        game.status = Game.FINISHED
        game.save()
        template_name = "finish.html"
    elif game.on_mission == True:
        template_name = "mission.html"
    else:
        context.update({'step': game_step.step})
        if game.mode == Game.ATTACK:
            template_name = "attack.html"
        elif game_step.is_puzzle_solved and game.mode == Game.CYPHER:
            template_name = "puzzle_solved.html"
        else:
            template_name = "puzzle.html"

    set_timer(request, context)
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context,
                                         request))


@login_required
def check_puzzle_answer(request):
    if request.method == 'POST':
        puzzle_answer = request.POST.get('puzzle_answer')
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        game_step = GameStep.objects.get(game=game,
        step__order=game.get_current_station)

        if game_step.step.puzzle.puzzle_answer == puzzle_answer.lower():
            game_step.is_puzzle_solved = True
            game_step.save()
    return redirect('game')


def not_found(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request))


@login_required(login_url='/')
def get_attack(request, attack_uuid):
    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        game_step = GameStep.objects.get(game=game,
                                         step__attack__attack_uuid=attack_uuid,
                                         step__order=game.get_current_station
                                         )
    except Game.DoesNotExist:
        return redirect('not_found')
    except GameStep.DoesNotExist:
        try:
            message = f'Attack not found! Current_station: {game.get_current_station} || UUID: {attack_uuid}'
            log = Log.objects.create(user=request.user, message=message)
            log.save()
        except Exception as e:
            print(e)
        return redirect('not_found')

    game.mode = Game.ATTACK
    game.save()

    return redirect('game')


@login_required
def story(request, story_id):
    if story_id < 0 or story_id > 6:
        return redirect('index')

    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        game_step = game.current_step

        if story_id is 0:
            game.mode = Game.CYPHER
            game.save()
            return redirect('game')

        context = {
            'game': game,
            'page_title': game.mode.upper() if not game.on_mission else 'mission',
            'mode': game.mode.lower() if not game.on_mission else 'mission'
        }
    except Game.DoesNotExist:
        return redirect('index')

    context.update({'step': game_step.step})
    template = loader.get_template(f'story/intro{story_id}.html')
    return HttpResponse(template.render(context, request))


# TODO: add logic for this template
def product(request, product_id):
    if product_id < 0 or product_id > 5:
        return redirect('index')

    context = {
        'page_title': 'STORY',
        'mode': 'story'
    }

    template = loader.get_template(f'story/product{product_id}.html')
    return HttpResponse(template.render(context, request))

