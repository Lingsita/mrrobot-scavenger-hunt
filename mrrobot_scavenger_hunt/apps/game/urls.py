from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('start', views.start_game, name='start'),
    path('finish', views.finish_game, name='finish'),
    path('game', views.game, name='game'),
]
