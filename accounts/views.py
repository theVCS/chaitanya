  
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request,"accounts/home.html", context)