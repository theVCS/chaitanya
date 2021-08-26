from collections import UserList
from django.shortcuts import render
from django.http import HttpResponse
import json
from . mailer import send_mail
from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from random import randint
from django.contrib.auth import logout

# Create your views here.

Profile = apps.get_model('profiles', 'Profile')


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def resetAccount(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }

    email = request.POST.get("email")

    cnt = 0
    if Profile.objects.filter(email=email).exists():
        cnt = 1

    if cnt == 0:
        context["err"] = "no such account exists"
        return render(request, "registration/login.html", context)

    otp = random_with_N_digits(6)
    context["otp"] = otp
    context["username"] = Profile.objects.filter(email=email)[0].user
    send_mail("Reset Password From Chaitanya", "Your previous username is {} and otp is {}".format(
        context["username"], otp), [email, ])
    return render(request, "accounts/resetAccount.html", context)


def resetPass(request):
    username = request.POST.get("username")
    password = request.POST.get("password1")
    user = User.objects.get(username=username)
    user.set_password(password)
    user.save()
    user = authenticate(username=username, password=password)
    login(request, user)
    return render(request, "home/home.html")


def home(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request, "accounts/home.html", context)


def logout_view(request):
    logout(request)
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request, "registration/login.html", context)


def checkUserName(request):
    username = request.POST.get("username")
    cnt = 0
    if User.objects.filter(username=username).exists():
        cnt = 1
    data = json.dumps({
        'cnt': cnt,
    })
    return HttpResponse(data)


def checkEmail(request):
    email = request.POST.get("email")
    cnt = 0
    if Profile.objects.filter(email=email).exists():
        cnt = 1
    data = json.dumps({
        'cnt': cnt,
    })
    return HttpResponse(data)


def addUser(request):
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
        username = user_form.cleaned_data['username']
        password = user_form.cleaned_data['password1']
        user = authenticate(username=username, password=password)
        login(request, user)
        return render(request, 'home/home.html', {"title": "Chaitanya - vision to impart knowledge"})
    else:
        return render(request, 'accounts/home.html', {"title": "Chaitanya - vision to impart knowledge"})


def createAccount(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        otp = random_with_N_digits(6)
        send_mail("Thanks for joining Chaintanya", otp, [email, ])
        context = {
            "title": "Chaitanya - vision to impart knowledge",
            "username": username,
            "password": password,
            "firstName": firstName,
            "lastName": lastName,
            "email": email,
            "phone": phone,
            "otp": otp,
        }
        return render(request, 'accounts/otpConfirm.html', context)
    else:
        return render(request, 'accounts/home.html', {"title": "Chaitanya - vision to impart knowledge"})


def profile(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request, "home/home.html", context)
