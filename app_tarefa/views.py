from django.shortcuts import render, redirect
from app_tarefa.models import Tarefa

def index(request):
    return render(request, 'app_tarefa/index.html')

def tarefas(request):  
    tarefas = Tarefa.objects.all()
    return render(request, 'app_tarefa/dashboard.html', {'tarefas': tarefas})

def create_novo(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data')
        status = False

        Tarefa.objects.create(titulo=titulo, descricao=descricao, data=data, status=status)
        return redirect('tarefas')
    return render(request, 'app_tarefa/create_novo.html')