from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('signup', views.signup, name='signup'),
    path('start', views.start_game, name='start'),
    path('game', views.game, name='game'),
    path('not_found', views.not_found, name='not_found'),
    path('attack/<uuid:attack_uuid>/', views.get_attack, name='get_attack')
]
