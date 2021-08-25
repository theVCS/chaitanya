from django.contrib import admin
from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.home, name='blogHome'),
    path('details/', views.blogDetails, name='blogDetails'),
    path('addComment/', views.addComment, name='addComment'),
    path('deleteComment/', views.deleteComment, name='deleteComment'),
]
