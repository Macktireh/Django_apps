from django.shortcuts import render, get_object_or_404
from apps.profiles.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

def profile(request, pseudo):
    profile = get_object_or_404(User, first_name=pseudo)
    template = "profiles/profiles.html"
    context = {'Profiles': profile}
    return render(request, template, context=context)
