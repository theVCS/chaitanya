from newsletters.models import Newsletter
from django.shortcuts import render, HttpResponse
from .models import Newsletter, Comment
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    newsletters = Newsletter.objects.all().reverse()
    context = {
        "title": "Chaitanya: Vision to impart knowledge",
        "newsletters": newsletters,
    }
    return render(request, "newsletters/home.html", context)

def showDetails(request):
    id = request.GET.get("newsletter")
    context = {
        "title": "Chaitanya: Vision to impart knowledge",
        "newsletterId": id,
        "newsletter": Newsletter.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(newsletterId=id),
    }
    return render(request, "newsletters/newsletterDetails.html", context)

def addComment(request):
    id = request.POST.get("newsletterId")
    user = request.POST.get("user")
    cmt = request.POST.get("comment")

    newsletter = Newsletter.objects.filter(id=id)[0]
    newsletter.commentsCnt = newsletter.commentsCnt + 1
    newsletter.save()

    comment = Comment.objects.create(newsletterId=newsletter, owner=request.user, details=cmt)
    comment.save()

    context = {
        "title": "Chaitanya: Vision to impart knowledge",
        "newsletterId": id,
        "newsletter": Newsletter.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(newsletterId=id),
    }

    return render(request, "newsletters/newsletterDetails.html", context)

def deleteComment(request):
    cmtid = request.GET.get("id")
    cmt = Comment.objects.get(pk=cmtid)
    cmt.delete()

    id = request.GET.get("newsletterId")
    newsletter = Newsletter.objects.filter(id=id)[0]
    newsletter.commentsCnt = newsletter.commentsCnt - 1
    newsletter.save()

    context = {
        "title": "Chaitanya: Vision to impart knowledge",
        "newsletterId": id,
        "newsletter": Newsletter.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(newsletterId=id),
    }

    return render(request, "newsletters/newsletterDetails.html", context)
