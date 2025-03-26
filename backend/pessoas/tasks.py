from .models import Pessoa

def create_pessoa(dto):
    pessoa = Pessoa.objects.create(**dto)
    return pessoa

def update_pessoa(pessoa_id, dto):
    pessoa = Pessoa.objects.get(pk=pessoa_id)
    for key, value in dto.items():
        setattr(pessoa, key, value)
    pessoa.save()
    return pessoa

def delete_pessoa(pessoa_id):
    Pessoa.objects.filter(pk=pessoa_id).delete()

def get_pessoa(pessoa_id):
    return Pessoa.objects.get(pk=pessoa_id)

def list_pessoas():
    return Pessoa.objects.all()
