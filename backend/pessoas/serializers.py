from rest_framework import serializers
from pessoas.models import Pessoa


class PessoaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'
