from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from ztoweb.forms import HeroForm, ProfileForm, LoginForm
from ztoweb.models import Hero, User, Profile


# Create your views here.
def home(req):
    return render(req, 'home.html')

def heroes(request):
    hero_list = Hero.objects.all()
    return render(request, "heroes/hero_list.html", {"heroes":hero_list})

def create_hero(request):
    context = {}
    form = HeroForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('heroes')

    context['form'] = form
    return render(request, "heroes/create_hero.html", context)

def hero_details(request, id):
    context = {}

    context['hero'] = Hero.objects.get(id=id)
    return render(request, "heroes/hero_view.html", context)

def profiles(request):
    profile_list = Profile.objects.all()
    return render(request, "profiles/profile_list.html", {"profiles":profile_list})

def register(request):
    context = {}
    form = ProfileForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('profiles')

    context['form'] = form
    return render(request, "profiles/register_profile.html", context)

def login(request):
    context = {}
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            return redirect('home')

    context['form'] = form
    return render(request, "profiles/profile_login.html", context)
