from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request,"homes/home.html", context)