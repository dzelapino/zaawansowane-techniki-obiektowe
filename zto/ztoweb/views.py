from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from ztoweb.forms import HeroForm
from ztoweb.models import Hero, User


# Create your views here.
def home(req):
    return render(req, 'home.html')

def heroes(request):
    hero_list = Hero.objects.all()
    return render(request, "heroes/hero_list.html", {"heroes":hero_list})

def create_hero(request):
    context = {}

    form = HeroForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "heroes/create_hero.html", context)

def hero_details(request, id):
    context = {}

    context['hero'] = Hero.objects.get(id=id)
    return render(request, "heroes/hero_view.html", context)

def users(request):
    user_list = User.objects.all()
    return render(request, "users/users_list.html", {"users":user_list})

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("heroes")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})