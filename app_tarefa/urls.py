from django.urls import path
from app_tarefa.views import index

urlpatterns = [
   path('',index, name='index')
]