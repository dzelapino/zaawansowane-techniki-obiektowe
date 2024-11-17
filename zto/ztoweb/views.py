from pyexpat.errors import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login, authenticate, logout

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

def login_view(request):
    context = {}

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create_hero')
    else:
        form = AuthenticationForm()

    context['form'] = form
    return render(request, "profiles/profile_login.html", context)



    # return render(request, "profiles/profile_login.html", context)

    # form = LoginForm(request.POST or None)
    #
    # if request.method == "POST":
    #     if form.is_valid():
    #         return redirect('home')
    #
    # context['form'] = form
    # return render(request, "profiles/profile_login.html", context)

def logout_view(request):
    logout(request)
    return redirect('home')