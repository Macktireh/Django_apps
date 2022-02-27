from django.shortcuts import render



def sign_up(request):
    template = "users/sign_up.html"
    context = {}
    return render(request, template, context=context)
    

def sing_in(request):
    template = "users/sign_in.html"
    context = {}
    return render(request, template, context=context)


def user_logout(request):
    template = "users/logout.html"
    context = {}
    return render(request, template, context=context)