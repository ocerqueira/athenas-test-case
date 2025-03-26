from django.db import models

class Pessoa(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    cpf = models.CharField(max_length=11)
    altura = models.IntegerField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    
