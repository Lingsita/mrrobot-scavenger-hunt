from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as log_out
from django.contrib.auth.models import User

from mrrobot_scavenger_hunt.apps.game.models import Game, GameStep, Path


def index(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context = {
                'game_in_progress': False,
                'page_title': 'HACKER SETUP'
            }
        else:
            context = {
                'message': 'invalid_credentials. Please try again',
            }

    template = loader.get_template('index.html')

    return HttpResponse(template.render(context, request))


def signup(request):
    context = {}
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
                game, _ = Game.objects.get_or_create(user=user, path=paths[counter])
                game.start()
                counter+=1
            message = "Game Started!!"
        else:
            message = "Hay mas jugadores que path, configurelo por admin"

    template = loader.get_template('index.html')

    return HttpResponse(template.render({'message': message,
                                         'already_started': already_started},
                                         request))

@login_required
def game(request):
    try:
        game = Game.objects.get(user=request.user)
        game_step = game.current_step
        if request.method == 'POST' and 'puzzle_answer' in request.POST:
            puzzle_answer = request.POST.get('puzzle_answer')
            if game_step.step.puzzle.answer.lower() == puzzle_answer.lower():
                game_step.is_puzzle_solved = True
                game_step.save()
        context = {'game': game,
                   'message': 'Hurry Up!',
                   'page_title': game.mode.upper(),
                 }
    except Game.DoesNotExist:
        return redirect('index')

    if game.status == Game.FINISHED:
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

    template = loader.get_template(template_name)
    return HttpResponse(template.render(context,
                                         request))


@login_required
def check_puzzle_answer(request):
    if request.method == 'POST':
        puzzle_answer = request.POST.get('puzzle_answer')
        game = Game.objects.get(user=request.user)
        game_step = GameStep.objects.get(game=game,
        step__order=game.get_current_station)

        if game_step.step.puzzle.puzzle_answer == puzzle_answer.lower():
            game_step.is_puzzle_solved = True
            game_step.save()
    return redirect('game')


@login_required
@staff_member_required
def finish_game(request):
    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        game.status = Game.FINISHED
        game.end_date = datetime.now()
        game.save()
        message = 'Game Over'
    except Game.DoesNotExist:
        return redirect('index')

    template = loader.get_template('game.html')

    return HttpResponse(template.render({'game': game, 'message': message}, request))


@login_required
@staff_member_required
def next_station(request):
    try:
        game = Game.objects.get(user=request.user, status=Game.IN_PROGRESS)
        game.status = Game.FINISHED
        game.end_date = datetime.now()
        game.save()
        message = 'Game Over'
    except Game.DoesNotExist:
        return redirect('index')

    template = loader.get_template('game.html')

    return HttpResponse(template.render({'game': game, 'message': message}, request))


def not_found(request):
    template = loader.get_template('not_found.html')
    return HttpResponse(template.render({}, request))


@login_required
def get_attack(request, attack_uuid):
    try:
        game = Game.objects.get(user=request.user)
        game_step = GameStep.objects.get(game__user=request.user,
                                         step__attack__attack_uuid=attack_uuid,
                                         step__order=game.get_current_station
                                         )
    except GameStep.DoesNotExist:
        return redirect('not_found')

    template = loader.get_template('attack.html')

    return HttpResponse(template.render({'attack': game_step.step.attack, 'message': 'ok'}, request))
