from django.shortcuts import render


def profile(request):
    template = "profiles/profiles.html"
    context = {}
    return render(request, template, context=context)
