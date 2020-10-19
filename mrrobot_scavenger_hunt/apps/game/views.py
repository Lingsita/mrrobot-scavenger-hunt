from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader

from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as log_out
from django.contrib.auth.models import User


def index(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    context = {}
    print(user)
    if user is not None:
        login(request, user)
        context.update({
            'game_in_progress': False,
        })
    else:
        context.update({
            'message': 'invalid_credentials. Please try again',
        })

    template = loader.get_template('index.html')

    return HttpResponse(template.render(context, request))


def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    context = {
        'message': 'Please enter your information',
    }
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

    template = loader.get_template('signup.html')

    return HttpResponse(template.render(context, request))


def logout(request):
    log_out(request)
    template = loader.get_template('logout.html')
    return HttpResponse(template.render({}, request))


@login_required
def game(request):
    '''
        shows all challenges/questions
    :param request:
    :return:
    '''


@login_required
def start_game(request):
    '''
        Each player can start his own game, it will generate a path
    :param request:
    :return:
    '''


@login_required
def finish_game(request):
    '''
        If superuser_ can finish the game
    :param request:
    :return:
    '''


@login_required
def score_board(request):
    '''
        Show results
    :param request:
    :return:
    '''


@login_required
def send_answer(request):
    '''
        Show results
    :param request:
    :return:
    '''
