from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Thread

from .forms import CreateUserForm, CreateCommentForm, CreateThreadForm, DeleteThreadForm


def home_page(request):
    return render(request, "home.html", {})


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def dashboard_page(request):
    threads = Thread.objects.all()
    return render(request, 'dashboard.html', {'threads': threads})


def create_thread(request):
    if request.method == 'GET':
        form = CreateThreadForm()
    else:
        form = CreateThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}

    return render(request, 'create_thread.html', context)


def edit_thread(request, pk):
    thread = Thread.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CreateThreadForm(instance=thread)
    else:
        form = CreateThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_details', pk=thread.pk)

    context = {'form': form, 'thread': thread}

    return render(request, 'edit_thread.html', context)


def delete_thread(request, pk):
    thread = Thread.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = DeleteThreadForm(instance=thread)
    else:
        form = DeleteThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form, 'thread': thread}

    return render(request, 'delete_thread.html', context)


def thread_details(request, pk):
    thread = Thread.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = thread
            comment.save()
            return redirect('thread_details', pk=thread.pk)
    else:
        form = CreateCommentForm()

    return render(request, 'thread_details.html', {'thread': thread, 'form': form})


def calculator_page(request):
    return render(request, 'calculator.html', {})