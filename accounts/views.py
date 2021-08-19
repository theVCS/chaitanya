from collections import UserList
from django.shortcuts import render
from django.http import HttpResponse
import json
from . mailer import send_mail
from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string

# Create your views here.

Profile = apps.get_model('profiles', 'Profile')


def home(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request, "accounts/home.html", context)


def checkUserName(request):
    username = request.POST.get("username")
    cnt = 0
    if User.objects.filter(username=username).exists():
        cnt = 1
    data = json.dumps({
        'cnt': cnt,
    })
    return HttpResponse(data)


def createAccount(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        user = user_form.save()
        user.save()
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        resume = request.FILES['resume']
        profile = Profile.objects.create(
            user=user, firstName=firstName, lastName=lastName, email=email, phone=phone, resume=resume)
        profile.save()
        message = render_to_string('../templates/accounts/email_template.html', {
            'title': "You are now a member",
        })
        send_mail("Thanks for joining Chaintanya", message, [email,])
        username = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'accounts/home.html', {"title": "Chaitanya - vision to impart knowledge"})
    else:
        return render(request, 'accounts/home.txt', {"title": "Chaitanya - vision to impart knowledge"})
