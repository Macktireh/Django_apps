from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.core.mail import send_mail, EmailMessage
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from apps.users.forms import Sign_UpForm
from apps.users.token import generateToken
from config.settings import EMAIL_HOST_USER

User = get_user_model()


def sign_up(request):
    if request.method == 'POST':
        user_form = Sign_UpForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.is_active = False
            user.save() 
            messages.success(request, "Votre compte à été bien enregistrer. \nVous recevez pour confirmer votre email.")
            
            current_site = get_current_site(request)
            
            # mail de bienvenue
            subject_welcome = f"Bienvenue {user.first_name} sur notre site"
            message_welcome = f"Bonjour {user.first_name} et Bienvenue sur notre site.\nNous très content de t'avoir parmis nous.\nMerci\nL'équipe {current_site}"
            from_email_welcome = EMAIL_HOST_USER
            to_email_welcome = [user.email]
            send_mail(subject_welcome, message_welcome, from_email_welcome, to_email_welcome, fail_silently=False)
            
            # mail d'activation du compte
            subject_confirm_email = f"Confirmer votre adresse mail de votre compte sur {current_site}"
            message_confirm_email = render_to_string('users/confirm_email.html', {
                'name': user.first_name,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'tokens': generateToken.make_token(user)
            })
            email_send = EmailMessage(subject_confirm_email, message_confirm_email, EMAIL_HOST_USER, [user.email])
            email_send.fail_silently = False
            email_send.send()
             
            return redirect('sign_in')
        else:
            messages.error(request, "Merci de bien remplir les informations correctement.")
    else:
        user_form = Sign_UpForm()
        
    template = 'users/sign_up.html'
    context = {
        'user_form': user_form,
    }
    return render(request, template, context=context)
    

def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, "Votre n'est pas encore activer.")
        else:
            messages.error(request, "ERREUR : votre email ou votre mot de passe est incorrect.")
        
    template = 'users/sign_in.html'
    context = {}
    return render(request, template, context=context)


def user_logout(request):
    logout(request)
    return redirect('home')


def activated_confirm_eamil_token(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and generateToken.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Votre compte à  été bien activer")
        return redirect('sign_in')
    else:
        messages.error(request, "Malhereussement votre compte n'a été activer")