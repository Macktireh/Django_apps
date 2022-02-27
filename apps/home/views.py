from django.shortcuts import render


def home(request):
    template = "home/index.html"
    context = {}
    return render(request, template, context=context)