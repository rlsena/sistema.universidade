from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo=models.CharField(max_length=6, primary_key=True)
    nome=models.CharField(max_length=50)
    professor=models.CharField(max_length=50)
    creditos=models.PositiveSmallIntegerField()

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nome, self.creditos)