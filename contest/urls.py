from django.contrib import admin
from django.urls import path, include
from contest import views

urlpatterns = [
    path('', views.contests, name='contestsHome'),
    path('details/', views.contestDetails, name='contestDetails'),
    path('addComment/', views.addComment, name='contestComment'),
    path('deleteComment/', views.deleteComment, name='deleteContestComment'),
    path('getResult/', views.getResult, name='getResult'),
    path('getPrevResult/', views.getPrevResult, name='getPrevResult'),
    path('getNextResult/', views.getNextResult, name='getNextResult'),
]