from pessoas.tasks import (
    create_pessoa,
    update_pessoa,
    delete_pessoa,
    get_pessoa,
    list_pessoas
)

def criar_pessoa_service(dto):
    """
    Cria uma nova pessoa.
    Aqui você pode incluir validações ou outras regras de negócio.
    """
    try:
        nova_pessoa = create_pessoa(dto)
        return nova_pessoa
    except Exception as e:
        raise Exception(f"Erro ao criar pessoa: {e}")

def atualizar_pessoa_service(pessoa_id, dto):
    """
    Atualiza os dados da pessoa identificada por pessoa_id.
    """
    try:
        pessoa_atualizada = update_pessoa(pessoa_id, dto)
        return pessoa_atualizada
    except Exception as e:
        raise Exception(f"Erro ao atualizar pessoa: {e}")

def excluir_pessoa_service(pessoa_id):
    """
    Exclui a pessoa com o ID informado.
    """
    try:
        delete_pessoa(pessoa_id)
    except Exception as e:
        raise Exception(f"Erro ao excluir pessoa: {e}")

def buscar_pessoa_service(pessoa_id):
    """
    Retorna a pessoa com base no ID.
    """
    try:
        return get_pessoa(pessoa_id)
    except Exception as e:
        raise Exception(f"Erro ao buscar pessoa: {e}")

def listar_pessoas_service():
    """
    Retorna todas as pessoas cadastradas.
    """
    try:
        return list_pessoas()
    except Exception as e:
        raise Exception(f"Erro ao listar pessoas: {e}")


def calcular_peso_ideal(pessoa):
    """
    Calcula o peso ideal com base na altura (convertida para metros) e no sexo.
    Fórmulas:
      - Homens: (72.7 * altura_em_metros) - 58
      - Mulheres: (62.1 * altura_em_metros) - 44.7
    """
    # Converter a altura para metros (se armazenada em centímetros)
    altura_em_metros = pessoa.altura / 100.0
    if pessoa.sexo.upper() == 'M':
        peso_ideal = (72.7 * altura_em_metros) - 58
    elif pessoa.sexo.upper() == 'F':
        peso_ideal = (62.1 * altura_em_metros) - 44.7
    else:
        peso_ideal = None
    return round(peso_ideal, 2) if peso_ideal is not None else None
