# Projeto de Controle de Pedidos de Água

### Trabalho desenvolvido para disciplina de fundamentos de banco de dados (FBD), UFC - quixadá - 2024.2

## Configuração do Ambiente

1. Clone o repositório:
    ```sh
    git clone <URL_DO_REPOSITORIO>
    cd app-agua
    ```

2. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```

3. Ative o ambiente virtual:
    - No Windows:
        ```sh
        venv\Scripts\activate
        ```
    - No macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

5. Não precisa desse passo. Crie um arquivo `.env` na raiz do projeto com as seguintes configurações:
    ```
    SECRET_KEY=your_secret_key
    DEBUG=True
    DB_NAME=your_db_name
    DB_USER=your_db_user
    DB_PASSWORD=your_db_password
    DB_HOST=your_db_host
    DB_PORT=your_db_port
    ```

6. Faça as migrations e crie o banco de dados:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Crie um superusuário para acessar o admin do Django:
    ```sh
    python manage.py createsuperuser
    ```

8. Inicie o servidor:
    ```sh
    python manage.py runserver
    ```

9. Acesse o projeto no navegador:
    ```
    http://127.0.0.1:8000/
    ```

## Estrutura do Projeto

- `appagua/`: Diretório principal do projeto Django.
- `loja/`: Aplicação principal contendo as views, models e templates.
- `templates/`: Diretório contendo os templates HTML.
- `static/`: Diretório contendo arquivos estáticos (CSS, JS, imagens).

## Funcionalidades

- Gerenciamento de Usuários
- Gerenciamento de Clientes
- Gerenciamento de Entregadores
- Gerenciamento de Produtos
````
