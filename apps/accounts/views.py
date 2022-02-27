from django.shortcuts import render



def sign_up(request):
    template = "accounts/sign_up.html"
    context = {}
    return render(request, template, context=context)
    

def sing_in(request):
    template = "accounts/sign_in.html"
    context = {}
    return render(request, template, context=context)


def user_logout(request):
    template = "accounts/logout.html"
    context = {}
    return render(request, template, context=context)