# Escolhe uma imagem base com Python instalado
FROM python:3.13-slim

# Instala dependências necessárias para compilar pacotes e para o psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Define o diretório de trabalho dentro do container
WORKDIR /code

# Copia o arquivo de requisitos para o container
COPY requirements.txt /code/

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o restante do código para o container
COPY . /code/

# Expõe a porta que o Django usará
EXPOSE 8000

# Comando padrão para iniciar a aplicação (pode ser sobrescrito pelo docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
