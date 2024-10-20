from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from ztoweb.forms import HeroForm
from ztoweb.models import Hero


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
