from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path("mojprofil/", views.myprofile, name='myprofile'),
    # path("izmjenalozinke/", auth_views.PasswordChangeView.as_view(template_name='core/changepassword.html'), name='changepassword'),
    path("izmjenalozinke/",views.changepassword, name='changepassword'),
    path("sync",views.sync, name="sync"),
]
