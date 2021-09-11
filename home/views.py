from django.shortcuts import render, HttpResponse
import json
from .models import Gallery

# Create your views here.
def home(request):
    return render(request,'home/home.html')


def gallery(request):
    context = {}
    lmt = 10
    query = Gallery.objects.order_by('-pk')
    lmt = min(lmt, query.count())
    query = query[:lmt]
    
    context["img"] = []

    for q in query:
        context["img"].append(q.img.url)
        
    return HttpResponse(json.dumps(context))