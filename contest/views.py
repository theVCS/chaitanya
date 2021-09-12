from typing import ContextManager
from django import http
from django.shortcuts import render, HttpResponse
import json
from django.apps import apps
from pandas.core.indexes.base import Index
from .models import Contest, Comment
import pandas as pd
# Create your views here.


def contests(request):
    lmt = 15
    contests = Contest.objects.order_by('-pk')
    lmt = min(lmt, contests.count())
    contests = contests[:lmt]

    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "contests": contests,
    }
    return render(request, "contests/home.html", context)


def contestDetails(request):
    id = request.GET.get("contest")
    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "contestId": id,
        "contest": Contest.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(contestId=id),
    }

    if(context["contest"].result):
        context["resultUploaded"] = 1
    else:
        context["resultUploaded"] = 0

    return render(request, "contests/contestDetails.html", context)


def addComment(request):
    id = request.POST.get("contestId")
    user = request.POST.get("user")
    cmt = request.POST.get("comment")

    contest = Contest.objects.filter(id=id)[0]
    contest.commentsCnt = contest.commentsCnt + 1
    contest.save()

    comment = Comment.objects.create(
        contestId=contest, owner=request.user, details=cmt)
    comment.save()

    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "contestId": id,
        "contest": Contest.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(contestId=id),
    }

    return render(request, "contests/contestDetails.html", context)


def deleteComment(request):
    cmtid = request.GET.get("id")
    cmt = Comment.objects.get(pk=cmtid)
    cmt.delete()

    id = request.GET.get("contestId")
    contest = Contest.objects.filter(id=id)[0]
    contest.commentsCnt = contest.commentsCnt - 1
    contest.save()

    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "contestId": id,
        "contest": Contest.objects.filter(id=id)[0],
        "comments": Comment.objects.filter(contestId=id),
    }

    return render(request, "contests/contestDetails.html", context)


def getResult(request):
    page = 1
    id = request.GET.get("contest")
    try:
        page = int(request.GET.get("page"))
    except:
        pass


    # context data
    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "columns": ["Index", ], # will contain the columns in the dataframe
        "left": 1, # true if going to prev page is possible
        "right": 1, # true if going to next page is possible
        "contestId": id, # the id of the contest
        "page": page,
    }


    contest = Contest.objects.get(pk=id)
    df = pd.read_csv(contest.result)
    # finding the number of pages [1, ceil(total_data/10)]
    context["pages"] = range(1, int((df.shape[0] + 9)/10)+1)


    # setting left and right pointer
    left = (page - 1) * 10
    right = (page * 10)
    right = min(df.shape[0], right)

    # if left zero then not possible to go to prev
    if left == 0:
        context["left"] = 0
    # if right is the end of data then not possible to 
    if right == df.shape[0]:
        context["right"] = 0

    df = df[left:right]


    # storing the data of the contestants
    lst = []

    for i in range(left+1,right+1):
        lst.append([i])

    for col in df.columns:
        context["columns"].append(col) # storing the column names

        index = 0
        
        for val in df[col]:
            lst[index].append(val)
            index += 1

    context["result"] = lst
    ####################################

    # return HttpResponse(json.dumps(context))
    return render(request, "contests/result.html",context)


def getPrevResult(request):
    page = 1
    id = request.GET.get("contest")
    try:
        page = int(request.GET.get("page")) - 1
    except:
        pass

    page = max(page,1)

    # context data
    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "columns": ["Index", ], # will contain the columns in the dataframe
        "left": 1, # true if going to prev page is possible
        "right": 1, # true if going to next page is possible
        "contestId": id, # the id of the contest
        "page": page,
    }


    # getting data frame and sorting it
    contest = Contest.objects.get(pk=id)
    df = pd.read_csv(contest.result)
    # finding the number of pages [1, ceil(total_data/10)]
    context["pages"] = range(1, int((df.shape[0] + 9)/10)+1)


    # setting left and right pointer
    left = (page - 1) * 10
    right = (page * 10)
    right = min(df.shape[0], right)

    # if left zero then not possible to go to prev
    if left == 0:
        context["left"] = 0
    # if right is the end of data then not possible to 
    if right == df.shape[0]:
        context["right"] = 0

    df = df[left:right]


    # storing the data of the contestants
    lst = []

    for i in range(left+1,right+1):
        lst.append([i])

    for col in df.columns:
        context["columns"].append(col) # storing the column names

        index = 0
        
        for val in df[col]:
            lst[index].append(val)
            index += 1

    context["result"] = lst
    ####################################

    # return HttpResponse(json.dumps(context))
    return render(request, "contests/result.html",context)


def getNextResult(request):
    page = 1
    id = request.GET.get("contest")

    try:
        page = int(request.GET.get("page")) + 1
    except:
        pass

    # context data
    context = {
        "title": "SOECE: Society Of Electronics And Communications",
        "columns": ["Index", ], # will contain the columns in the dataframe
        "left": 1, # true if going to prev page is possible
        "right": 1, # true if going to next page is possible
        "contestId": id, # the id of the contest
        "page": page,
    }


    # getting data frame and sorting it
    contest = Contest.objects.get(pk=id)
    df = pd.read_csv(contest.result)
    page = min(page,df.shape[0])
    # finding the number of pages [1, ceil(total_data/10)]
    context["pages"] = range(1, int((df.shape[0] + 9)/10)+1)


    # setting left and right pointer
    left = (page - 1) * 10
    right = (page * 10)
    right = min(df.shape[0], right)

    # if left zero then not possible to go to prev
    if left == 0:
        context["left"] = 0
    # if right is the end of data then not possible to 
    if right == df.shape[0]:
        context["right"] = 0

    df = df[left:right]


    # storing the data of the contestants
    lst = []

    for i in range(left+1,right+1):
        lst.append([i])

    for col in df.columns:
        context["columns"].append(col) # storing the column names

        index = 0
        
        for val in df[col]:
            lst[index].append(val)
            index += 1

    context["result"] = lst
    ####################################

    # return HttpResponse(json.dumps(context))
    return render(request, "contests/result.html",context)