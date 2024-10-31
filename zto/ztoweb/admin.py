from django.contrib import admin

from ztoweb.models import Subscriber, Hero, User, Profile

# Register your models here.
admin.site.register(Subscriber)
admin.site.register(Hero)
admin.site.register(User)
admin.site.register(Profile)