from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages

class CustomLogin(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

def home(request):
    context={}
    return render(request, "myApp/home.html", context)


