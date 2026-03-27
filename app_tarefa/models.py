from django.db import models

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=False, blank=False)
    data = models.DateField()
    status = models.BooleanField()

    def __str__(self):
        return self.titulo
