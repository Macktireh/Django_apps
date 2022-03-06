from django.shortcuts import render
from apps.profiles.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

def profile(request, pseudo):
    if Profile.objects.filter(pseudo=pseudo).exists():
        profile = Profile.objects.get(pseudo=pseudo)
    else:
        profile = User.objects.get(first_name=pseudo)

    template = "profiles/profiles.html"
    context = {'Profiles': profile}
    return render(request, template, context=context)
