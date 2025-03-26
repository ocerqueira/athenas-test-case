from django.contrib import admin

from pessoas.models import Pessoa

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nasc', 'cpf', 'altura', 'peso', 'sexo')
    search_fields = ('nome', 'cpf', 'sexo')

admin.site.register(Pessoa, PessoaAdmin)