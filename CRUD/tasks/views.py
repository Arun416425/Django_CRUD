from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, RegistationForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegistationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegistationForm()
    return render(request, "register.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
        
    context = {"form": form}
    return render(request, "login.html", context)


def logout(request):
    auth.logout(request)
    return redirect("login")


def get_tasks(request):
    tasks = Task.objects.all()
    form = TaskForm()

    context = {
        "tasks": tasks,
        "form": form,
    }
    return render(request, "home.html", context)


@login_required(login_url="/login")
def post_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm()
    return render(request, "form.html", {"form": form, "task": None})


@login_required(login_url="/login")
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TaskForm(instance=task)
    context = {
        "task": task,
        "form": form,
    }
    return render(request, "form.html", context)


@login_required(login_url="/login")
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        task.delete()
        return redirect("home")

    return render(request, "delete.html", {"task": task})
