from django.urls import path
from app_tarefa.views import index, tarefas, create_novo

urlpatterns = [
   path('',index, name='index'),
   path('tarefas', tarefas, name='tarefas'),
   path('create', create_novo, name='create_novo'),
   path('editar/<int:id>', create_novo, name='editar_tarefa'),
   path('excluir/<int:id>', create_novo, name='excluir_tarefa'),

]