from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'app_tarefa/index.html')

def login_view(request):
    if request.method == 'POST':
        # Aqui o Django pega os dados do formulário
        user_nome = request.POST.get('username')
        user_pass = request.POST.get('password')
        
        # Simulação de autenticação (ou use o sistema do Django)
        user = authenticate(request, username=user_nome, password=user_pass)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard') # Redireciona para a URL chamada 'dashboard'
        else:
            return render(request, 'index.html', {'erro': 'Usuário inválido'})

    return render(request, 'index.html')
