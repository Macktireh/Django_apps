from apps.profiles.models import Profile
from django.shortcuts import render


def home(request):
    profile = Profile.objects.all()
    template = "home/index.html"
    context = {
        'start_animation': 'home',
        'profile': profile
    }
    return render(request, template, context=context)

def home1(request):
    profile = Profile.objects.all()
    template = "profiles/profiles.html"
    context = {
        'start_animation': 'blog',
        'profile': profile
    }
    return render(request, template, context=context)