from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def error_404_view(request, exception):
    return render(request, "404.html")


@login_required(login_url="login")
def index(request):
    return render(request, "index.html")


def registration(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    else:
        user_form = RegistrationForm()
    return render(request, "registration.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse("<h1>Disable Account</h1>")

            else:
                return HttpResponse("<h1>Invalid Login</h1>")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect("index")
