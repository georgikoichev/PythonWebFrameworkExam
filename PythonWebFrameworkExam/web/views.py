from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import Thread

from .forms import CreateUserForm, CreateCommentForm, CreateThreadForm, CalculatorForm, MathFunctionsForm

import math


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


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def dashboard_page(request):
    threads = Thread.objects.all()
    return render(request, 'dashboard.html', {'threads': threads})


@login_required
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


@login_required
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


@login_required
def delete_thread(request, pk):
    thread = Thread.objects.get(pk=pk)
    if request.method == 'POST':
        thread.delete()
        return redirect('dashboard')
    else:
        return render(request, 'delete_thread.html', {'thread': thread})


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


@login_required
def calculator_page(request):
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operation = form.cleaned_data['operation']
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    form.add_error('num2', 'Invalid Input')
                    return render(request, 'calculator.html', {'form': form})
                result = num1 / num2
            elif operation == 'power':
                result = num1 ** num2
            return render(request, 'calculator.html', {'form': form, 'result': result})
    else:
        form = CalculatorForm()
    return render(request, 'calculator.html', {'form': form})


@login_required
def functions_page(request):
    if request.method == 'POST':
        form = MathFunctionsForm(request.POST)
        if form.is_valid():
            num = form.cleaned_data['num']
            operation = form.cleaned_data['operation']
            if operation == 'square root':
                if num < 0:
                    form.add_error('num', 'Invalid Input')
                    return render(request, 'math_functions.html', {'form': form})
                result = math.sqrt(num)
            elif operation == 'sinus':
                num *= 0.0174532925
                result = math.sin(num)
            elif operation == 'cosine':
                num *= 0.0174532925
                result = math.cos(num)
            elif operation == 'tangent':
                num *= 0.0174532925
                result = math.tan(num)
            elif operation == 'cotangent':
                num *= 0.0174532925
                result = 1 / math.sqrt(num)
            return render(request, 'math_functions.html', {'form': form, 'result': result})
    else:
        form = MathFunctionsForm()
    return render(request, 'math_functions.html', {'form': form})
