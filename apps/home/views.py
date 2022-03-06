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