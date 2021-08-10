from typing import ContextManager
from django.shortcuts import render


def home(request):
    context = {
        "title": "Chaitanya - vision to impart knowledge"
    }
    return render(request, "home/home.html", context)
