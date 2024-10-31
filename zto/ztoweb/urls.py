from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('heroes', views.heroes, name='heroes'),
    path('heroes/create', views.create_hero, name='create_hero'),
    path('heroes/<id>', views.hero_details, name='hero_details'),
    path('profiles', views.profiles, name='profiles'),
    path('profiles/register', views.register, name='register'),
    path('profiles/login', views.login, name='login'),
]
