from django.urls import path
from app_tarefa.views import index, tarefas

urlpatterns = [
   path('',index, name='index'),
   path('tarefas', tarefas, name='tarefas'),

]