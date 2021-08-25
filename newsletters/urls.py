from django.contrib import admin
from django.urls import path, include
from newsletters import views

urlpatterns = [
    path('', views.home, name='newsletterHome'),
    path('details', views.showDetails, name='showDetails'),
    path('addComment/', views.addComment, name='addCommentNews'),
    path('deleteComment/', views.deleteComment, name='deleteComment'),
]
