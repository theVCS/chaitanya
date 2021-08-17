from django.urls import path
from . import views

app_name = 'Accounts'

urlpatterns = [
    path('', views.home, name="accountsHome"),
    path('createAccount/', views.createAccount, name="createAccount"),
    path('checkUserName/', views.checkUserName, name="checkUserName"),
]