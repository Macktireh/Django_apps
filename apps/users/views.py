from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout

from apps.users.forms import Sign_UpForm, Sign_InForm

User = get_user_model()


def sign_up(request):
    if request.method == 'POST':
        user_form = Sign_UpForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Votre compte à été bien enregistrer')
            return redirect('sign_in')
        else:
            messages.error(request, 'Merci de bien remplir les informations correctement')
    else:
        user_form = Sign_UpForm()
        
    template = "users/sign_up.html"
    context = {
        'user_form': user_form,
    }
    return render(request, template, context=context)
    

def sign_in(request):
    if request.method == 'POST':
        # signin_form = Sign_InForm(request.POST or None)
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        # print('user:', user)
        if user:
            if user.is_active:
                login(request, user)
                # messages.success(request, 'Bonjour , nous content te revoir :)')
                return redirect('home')
            else:
                messages.warning(request, "Votre n'est pas encore activer.")

        else:
            messages.error(request, "ERREUR : votre email ou votre mot de passe est incorrect")
    # else:
    #     signin_form = Sign_InForm()
        
    template = "users/sign_in.html"
    context = {
        # 'signin_form': signin_form
    }
    return render(request, template, context=context)


def user_logout(request):
    logout(request)
    return redirect('home')