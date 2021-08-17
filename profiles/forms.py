from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    firstName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastName = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Your Email Id'}))
    phone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    resume = forms.FileField(widget=forms.TextInput(attrs={'placeholder': 'Upload File'}))

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'email_id', 'phone_number', 'resume')


# class UserSearchForm(forms.Form):
#     username = forms.CharField(label="", max_length=50, widget=forms.TextInput
#     (attrs={'placeholder': 'Search Username'}))
