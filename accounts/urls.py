from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.home, name="accountsHome"),
    path('createAccount/', views.createAccount, name="createAccount"),
    path('checkUserName/', views.checkUserName, name="checkUserName"),
    path('checkEmail/', views.checkEmail, name="checkEmail"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('addUser/', views.addUser, name='addUser'),
    path('resetAccount/', views.resetAccount, name='resetAccount'),
    path('resetPass/', views.resetPass, name='resetPass'),
]