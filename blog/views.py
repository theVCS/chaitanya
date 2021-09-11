from django.shortcuts import render, HttpResponse
from .models import Blog, Comment
from django.contrib.auth.models import User

# Create your views here.


def home(request):
    lmt = 15
    blog = Blog.objects.order_by('-pk')
    lmt = min(lmt,blog.count())
    blog = blog[:lmt]

    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "blogs": blog,
    }
    return render(request, "blog/home.html", context)


def blogDetails(request):
    id = request.GET.get("blog")
    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "blogId": id,
        "blog": Blog.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(blogId=id),
    }
    return render(request, "blog/blogDetails.html", context)


def addComment(request):
    id = request.POST.get("blogId")
    user = request.POST.get("user")
    cmt = request.POST.get("comment")

    blog = Blog.objects.filter(id=id)[0]
    blog.commentsCnt = blog.commentsCnt + 1
    blog.save()

    comment = Comment.objects.create(blogId=blog, owner=request.user, details=cmt)
    comment.save()

    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "blogId": id,
        "blog": Blog.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(blogId=id),
    }

    return render(request, "blog/blogDetails.html", context)

def deleteComment(request):
    cmtid = request.GET.get("id")
    cmt = Comment.objects.get(pk=cmtid)
    cmt.delete()

    id = request.GET.get("blogId")
    blog = Blog.objects.filter(id=id)[0]
    blog.commentsCnt = blog.commentsCnt - 1
    blog.save()

    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "blogId": id,
        "blog": Blog.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(blogId=id),
    }

    return render(request, "blog/blogDetails.html", context)