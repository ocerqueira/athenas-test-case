from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.response import Response
from pessoas.serializers import PessoaModelSerializer
from pessoas.services import (
    criar_pessoa_service, atualizar_pessoa_service,
    excluir_pessoa_service, buscar_pessoa_service,
    listar_pessoas_service, calcular_peso_ideal
)

class PessoaModelViewSet(viewsets.ViewSet):
    
    def list(self, request):
        pessoas = listar_pessoas_service()
        serializer = PessoaModelSerializer(pessoas, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        pessoa = buscar_pessoa_service(pk)
        serializer = PessoaModelSerializer(pessoa)
        return Response(serializer.data)

    def create(self, request):
        serializer = PessoaModelSerializer(data=request.data)
        if serializer.is_valid():
            nova_pessoa = criar_pessoa_service(serializer.validated_data)
            return Response(
                PessoaModelSerializer(nova_pessoa).data,
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        serializer = PessoaModelSerializer(data=request.data)
        if serializer.is_valid():
            pessoa_atualizada = atualizar_pessoa_service(pk, serializer.validated_data)
            return Response(PessoaModelSerializer(pessoa_atualizada).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk=None):
 
        pessoa = buscar_pessoa_service(pk)
        serializer = PessoaModelSerializer(pessoa, data=request.data, partial=True)
        if serializer.is_valid():
            pessoa_atualizada = atualizar_pessoa_service(pk, serializer.validated_data)
            return Response(PessoaModelSerializer(pessoa_atualizada).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        excluir_pessoa_service(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['get'], url_path='peso-ideal')
    def peso_ideal(self, request, pk=None):
        try:
            pessoa = buscar_pessoa_service(pk)
            peso_ideal = calcular_peso_ideal(pessoa)
            return Response({
                'id': pessoa.id,
                'nome': pessoa.nome,
                'peso_ideal': peso_ideal
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
