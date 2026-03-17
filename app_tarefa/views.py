from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'app_tarefa/index.html')

def tarefas(request):  
    return render(request, 'app_tarefa/dashboard.html')

