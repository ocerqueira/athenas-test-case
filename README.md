# Projeto Athenas


## Pré-requisitos

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuração

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/ocerqueira/athenas-test-case.git
   cd <nome_do_repositorio>
   ```

2. **Variáveis de Ambiente**

   Crie um arquivo `.env` na raiz do projeto e defina as seguintes variáveis:

   ```env
   DATABASE_NAME=nome_do_banco
   DATABASE_USER=usuario
   DATABASE_PASSWORD=senha
   ```

## Como Executar

1. **Construir e Iniciar os Containers**

   Execute o comando abaixo para construir e iniciar todos os containers (backend, frontend e banco de dados):

   ```bash
   docker-compose up --build
   ```

   - O serviço **backend** executa as migrações automaticamente usando o script `wait-for-it.sh` para aguardar o banco de dados estar disponível.
   - O serviço **frontend** serve os arquivos estáticos via Nginx.
   - O serviço **db** é um container PostgreSQL configurado com as variáveis do arquivo `.env`.

2. **Acessar a Aplicação**

   - **Frontend:** Acesse [http://localhost](http://localhost) para ver a interface do usuário.
   - **Backend (API):** O servidor Django estará disponível em [http://localhost:8000](http://localhost:8000).

3. **Atualizar a Lista de Pessoas**

   No frontend, utilize o botão "Pesquisar" para recarregar os dados da API.

## Containers Personalizados

Os containers são nomeados conforme abaixo para facilitar a identificação:

- **Banco de Dados:** `atehanas-db`
- **Backend:** `backend-athenas`
- **Frontend:** `athenas-frontend`

## Parar os Containers

Para interromper a aplicação, pressione `Ctrl+C` no terminal onde o `docker-compose` está em execução e, em seguida, execute:

```bash
docker-compose down
```

## Considerações

- O script `wait-for-it.sh` no backend garante que o container do banco de dados esteja pronto antes de iniciar as migrações e o servidor Django.
- Esta aplicação foi configurada para servir somente arquivos estáticos no frontend. Qualquer funcionalidade de busca ou filtragem na API deve ser implementada no backend se necessário.

