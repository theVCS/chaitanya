from typing import ContextManager
from django.shortcuts import render, HttpResponse
import json
from .models import Gallery
from django.apps import apps
from datetime import date, datetime, timezone
import pytz


Blog = apps.get_model('blog', 'Blog')
Newsletter = apps.get_model('newsletters', 'Newsletter')
Contest = apps.get_model('contest', 'Contest')

# Create your views here.


def home(request):
    context = {
        "title": "SOECE: Society Of Electronics And Communications"
    }
    return render(request, 'home/home.html', context)


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


def notifications(request):
    utc = pytz.UTC

    context = {}
    context["blogs"] = []
    context["newsletters"] = []

    lmt_from_blog = 10
    lmt_from_newsletter = 10
    lmt_from_contest = 10

    blog = Blog.objects.order_by('-pk')
    lmt_from_blog = min(lmt_from_blog, blog.count())
    blog = blog[:lmt_from_blog]

    newsletter = Newsletter.objects.order_by('-pk')
    lmt_from_newsletter = min(lmt_from_newsletter, newsletter.count())
    newsletter = newsletter[:lmt_from_newsletter]

    contest = Contest.objects.order_by('-pk')
    lmt_from_contest = min(lmt_from_contest, contest.count())
    contest = contest[:lmt_from_newsletter]

    now = utc.localize(datetime.now())

    for b in blog:
        data = {}
        data["heading"] = b.heading
        data["url"] = "blogs/details/?blog=" + str(b.pk)
        diff = (now - b.time).days

        if diff < 10:
            data["new"] = 1
        else:
            data["new"] = 0

        context["blogs"].append(data)

    for n in newsletter:
        data = {}
        data["heading"] = n.heading
        data["url"] = "newsletters/details?newsletter=" + str(n.pk)

        diff = (now - n.time).days

        if diff < 10:
            data["new"] = 1
        else:
            data["new"] = 0

        context["newsletters"].append(data)

    for n in contest:
        data = {}
        data["heading"] = n.heading
        data["url"] = "contest/details/?contest=" + str(n.pk)

        diff = (now - n.time).days

        if diff < 10:
            data["new"] = 1
        else:
            data["new"] = 0

        context["newsletters"].append(data)

    return HttpResponse(json.dumps(context))
