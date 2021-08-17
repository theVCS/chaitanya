from django.shortcuts import render
from django.http import HttpResponse
import json
from . mailer import send_mail
from django.apps import apps
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from profiles.forms import ProfileForm

Profile = apps.get_model('profiles', 'Profile')


def home(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request, "accounts/home.html", context)


def checkUserName(request):
    userName = request.POST.get("userName")
    cnt = 0  # find number of users from database having username as userName
    data = json.dumps({
        'cnt': cnt,
    })
    return HttpResponse(data)


def createAccount(request):
    print(request.POST)
    # if request.method == 'POST':
        # user_form = UserCreationForm(request.POST)
        # profile_form = ProfileForm(request.POST)
        # print(user_form)
        # if user_form.is_valid() and profile_form.is_valid():
            # user = user_form.save()
            # user.save()
            # first_name = profile_form.cleaned_data['first_name']
            # last_name = profile_form.cleaned_data['last_name']
            # email_id = profile_form.cleaned_data['email_id']
            # phone_number = profile_form.cleaned_data['phone_number']
            # resume = profile_form.cleaned_data['resume']
            # profile = Profile.objects.create(
            #     user=user, first_name=first_name, last_name=last_name, email_id=email_id, phone_number=phone_number)
            # profile.save()
            # username = user_form.cleaned_data['username']
            # password = user_form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # return HttpResponseRedirect(reverse('accounts/'))
        # context = {'user_form': user_form, 'profile_form': profile_form}
        # return render(request, 'accounts/', context)
    # else:
        # user_form = UserCreationForm()
        # profile_form = ProfileForm()
        # context = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'accounts/')
        # return render(request, 'accounts/', context)
