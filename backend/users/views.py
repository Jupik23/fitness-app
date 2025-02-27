from django.shortcuts import render, redirect
from .forms import Register
from django.contrib.auth import login

from django.contrib.auth.views import LoginView

# Create your views here.
def register(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("firstpage") 
    else:
        form = Register()

    return render(request, "users/register.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "users/login.html"