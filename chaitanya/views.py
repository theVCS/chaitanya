from typing import ContextManager
from django.shortcuts import render


def home(request):
    context = {
        "title": "SOECE: Society Of Electronics And Communications"
    }
    return render(request, "home/home.html", context)
