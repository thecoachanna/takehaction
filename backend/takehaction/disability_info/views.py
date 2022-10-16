from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User
from .forms import NewUserForm


def index(request):
    users = User.objects.count()
    context = {"users": users}
    return render(request, "index.html", context=context)


def profile(request):
    users = User.objects.count()
    context = {"users": users}
    return render(request, "profile.html", context=context)


def info(request):
    users = User.objects.count()
    context = {"users": users}
    return render(request, "info.html", context=context)


def create_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            login(request, user)
            return redirect("/")
        else: 
            context = {"Error" : "Error during form loading"}
            return render(request,'registration/create_user.html',context=context)
    else:
        form = NewUserForm()
        context = {"form": form}
        return render(request, "registration/create_user.html", context=context)
