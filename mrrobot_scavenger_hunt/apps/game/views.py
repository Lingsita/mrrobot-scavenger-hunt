import unicodedata

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as log_out
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.template import loader
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from mrrobot_scavenger_hunt.apps.game.models import Game, GameStep, Path, Log
from mrrobot_scavenger_hunt.apps.game.products import PRODUCTS


@csrf_exempt
def index(request):
    context = {
        'mode': 'attack'
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username.lower(), password=password)
        if user is not None:
            login(request, user)
            context.update({
                'game_in_progress': False
            })
        else:
            context.update({
                'message': 'El usuario no es válido. Intenta de nuevo.',
            })

    set_timer(request, context)
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def set_timer(request, context):
    ms = -1
    if request.user.is_authenticated and not request.user.is_staff:
        try:
            game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
            current_time = timezone.now()
            diff = current_time - game.start_date
            ms = diff.seconds * 1000
        except Game.DoesNotExist:
            pass
    context["timer_ms"] = ms


@csrf_exempt
def signup(request):
    context = {
        'page_title': 'REGISTRO',
        'mode': 'attack'
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
            context['message'] = "Este usuario ya existe"
        except User.DoesNotExist:
            if username and password:
                user = User.objects.create(username=username.lower())
                user.set_password(password)
                user.save()
                return redirect('index')
            else:
                context['message'] = "Diligencia ambos campos"
    else:
        context['message'] = 'Ingresa tus datos'

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
            if check_answer(game_step.step.puzzle.answer, puzzle_answer):
                game_step.is_puzzle_solved = True
                save_log(request.user, 'Puzzle solved')
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
    elif game.mode == Game.STORY:
        template_name = "story/intro1.html"
    else:
        context.update({'step': game_step.step})
        if game.mode == Game.ATTACK:
            current_product = PRODUCTS[game.score]
            context["product"] = current_product
            template_name = "attack.html"
        elif game_step.is_puzzle_solved and game.mode == Game.CYPHER:
            template_name = "puzzle_solved.html"
        else:
            template_name = "puzzle.html"

    set_timer(request, context)
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


def check_answer(db_answer, user_answer):
    user_answer = user_answer.strip().lower()

    try:
        user_answer = unicode(user_answer, 'utf-8')
    except NameError:  # unicode is a default on python 3
        pass

    user_answer = unicodedata.normalize('NFD', user_answer)\
        .encode('ascii', 'ignore')\
        .decode("utf-8")

    return db_answer.lower() == user_answer


# @login_required
# def check_puzzle_answer(request):
#     if request.method == 'POST':
#         puzzle_answer = request.POST.get('puzzle_answer')
#         game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
#         game_step = GameStep.objects.get(game=game,
#         step__order=game.get_current_station)
#
#         if game_step.step.puzzle.puzzle_answer == puzzle_answer.lower():
#             game_step.is_puzzle_solved = True
#             game_step.save()
#     return redirect('game')


def not_found(request):
    template = loader.get_template('404.html')
    return HttpResponse(template.render({}, request))


@login_required(login_url='/')
def get_attack(request, attack_uuid):
    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        game_step = GameStep.objects.get(game=game,
                                         is_puzzle_solved=True,
                                         step__attack__attack_uuid=attack_uuid,
                                         step__order=game.get_current_station,
                                         )
    except Game.DoesNotExist:
        return redirect('not_found')
    except GameStep.DoesNotExist:
        message = f'Attack not found! Current_station: {game.get_current_station} || UUID: {attack_uuid}'
        save_log(request.user, message)
        return redirect('not_found')

    game.mode = Game.ATTACK
    game.save()

    return redirect('game')


def save_log(user, message):
    try:
        log = Log.objects.create(user=user, message=message)
        log.save()
    except Exception as e:
        print(e)


@login_required
def story(request, story_id):
    if story_id < 0 or story_id > 6:
        return redirect('index')

    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        if game.mode != Game.STORY:
            return redirect('game')

        context = {
            'game': game,
            'page_title': game.mode.upper() if not game.on_mission else 'mission',
            'mode': game.mode.lower() if not game.on_mission else 'mission'
        }

        if game.on_mission:
            template_name = "mission.html"
        elif story_id is 0:
            game.mode = Game.CYPHER
            game.save()
            return redirect('game')
        else:
            template_name = f'story/intro{story_id}.html'
    except Game.DoesNotExist:
        return redirect('index')

    context.update({'step': game.current_step.step})
    set_timer(request, context)
    template = loader.get_template(template_name)
    return HttpResponse(template.render(context, request))


@login_required
def deep_web_indicator(request):
    context = {
        'page_title': 'STORY',
        'mode': 'story',
        'timer_ms': -1
    }
    template = loader.get_template(f'deep_web_indicator.html')
    return HttpResponse(template.render(context, request))

@login_required
def listener(request):
    on_mission = False
    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        on_mission = game.on_mission
    except Game.DoesNotExist:
        pass

    return JsonResponse({
        'on_mission': on_mission
    })


@login_required
def mission(request):
    context = {
        'page_title': 'mission',
        'mode': 'mission',
        'timer_ms': -1
    }

    template = loader.get_template("mission.html")
    return HttpResponse(template.render(context, request))
