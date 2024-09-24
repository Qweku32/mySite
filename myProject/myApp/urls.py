from django.urls import path
from . import views 
from . forms import CustomLoginForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', auth_views.LoginView.as_view(form_class=CustomLoginForm), name='login'),    
]