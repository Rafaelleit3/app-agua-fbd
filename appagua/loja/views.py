from django.shortcuts import render, redirect
from django.db import connection

# Função auxiliar para executar consultas SQL
def execute_sql(query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        if query.strip().upper().startswith("SELECT"):
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        else:
            return cursor.rowcount

# Views para Usuario
def listar_usuarios(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        if usuario_id:
            query = """
                UPDATE loja_usuario SET nome=%s, sobrenome=%s, email=%s, cargo=%s, telefone=%s WHERE id=%s
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('sobrenome'),
                request.POST.get('email'),
                request.POST.get('cargo'),
                request.POST.get('telefone'),
                usuario_id
            )
            execute_sql(query, params)
        else:
            query = """
                INSERT INTO loja_usuario (nome, sobrenome, email, senha, cargo, telefone) VALUES (%s, %s, %s, %s, %s, %s)
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('sobrenome'),
                request.POST.get('email'),
                request.POST.get('senha'),
                request.POST.get('cargo'),
                request.POST.get('telefone')
            )
            execute_sql(query, params)
        return redirect('listar_usuarios')

    if 'delete' in request.GET:
        usuario_id = request.GET.get('delete')
        query = "DELETE FROM loja_usuario WHERE id=%s"
        execute_sql(query, [usuario_id])
        return redirect('listar_usuarios')

    query = "SELECT id, nome, sobrenome, email, cargo, telefone FROM loja_usuario"
    usuarios = execute_sql(query)
    return render(request, 'loja/usuarios.html', {'usuarios': usuarios})

# Views para Cliente
def listar_clientes(request):
    if request.method == 'POST':
        cliente_id = request.POST.get('cliente_id')
        if cliente_id:
            query = """
                UPDATE loja_cliente SET nome=%s, sobrenome=%s, endereco=%s, bairro=%s, cidade=%s, telefone=%s WHERE id=%s
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('sobrenome'),
                request.POST.get('endereco'),
                request.POST.get('bairro'),
                request.POST.get('cidade'),
                request.POST.get('telefone'),
                cliente_id
            )
            execute_sql(query, params)
        else:
            query = """
                INSERT INTO loja_cliente (nome, sobrenome, endereco, bairro, cidade, telefone) VALUES (%s, %s, %s, %s, %s, %s)
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('sobrenome'),
                request.POST.get('endereco'),
                request.POST.get('bairro'),
                request.POST.get('cidade'),
                request.POST.get('telefone')
            )
            execute_sql(query, params)
        return redirect('listar_clientes')

    if 'delete' in request.GET:
        cliente_id = request.GET.get('delete')
        query = "DELETE FROM loja_cliente WHERE id=%s"
        execute_sql(query, [cliente_id])
        return redirect('listar_clientes')

    query = "SELECT id, nome, sobrenome, endereco, bairro, cidade, telefone FROM loja_cliente"
    clientes = execute_sql(query)
    return render(request, 'loja/clientes.html', {'clientes': clientes})

# Views para Entregador
def listar_entregadores(request):
    if request.method == 'POST':
        entregador_id = request.POST.get('entregador_id')
        if entregador_id:
            query = """
                UPDATE loja_entregador SET nome=%s, sobrenome=%s, telefone=%s WHERE id=%s
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('sobrenome'),
                request.POST.get('telefone'),
                entregador_id
            )
            execute_sql(query, params)
        else:
            query = """
                INSERT INTO loja_entregador (nome, sobrenome, telefone) VALUES (%s, %s, %s)
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('sobrenome'),
                request.POST.get('telefone')
            )
            execute_sql(query, params)
        return redirect('listar_entregadores')

    if 'delete' in request.GET:
        entregador_id = request.GET.get('delete')
        query = "DELETE FROM loja_entregador WHERE id=%s"
        execute_sql(query, [entregador_id])
        return redirect('listar_entregadores')

    query = "SELECT id, nome, sobrenome, telefone FROM loja_entregador"
    entregadores = execute_sql(query)
    return render(request, 'loja/entregadores.html', {'entregadores': entregadores})

# Views para Produto
def listar_produtos(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        if produto_id:
            query = """
                UPDATE loja_produto SET nome=%s, status=%s, custo=%s, marca=%s, linha=%s, unidade=%s, valor=%s WHERE id=%s
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('status'),
                request.POST.get('custo'),
                request.POST.get('marca'),
                request.POST.get('linha'),
                request.POST.get('unidade'),
                request.POST.get('valor'),
                produto_id
            )
            execute_sql(query, params)
        else:
            query = """
                INSERT INTO loja_produto (nome, status, custo, marca, linha, unidade, valor) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            params = (
                request.POST.get('nome'),
                request.POST.get('status'),
                request.POST.get('custo'),
                request.POST.get('marca'),
                request.POST.get('linha'),
                request.POST.get('unidade'),
                request.POST.get('valor')
            )
            execute_sql(query, params)
        return redirect('listar_produtos')

    if 'delete' in request.GET:
        produto_id = request.GET.get('delete')
        query = "DELETE FROM loja_produto WHERE id=%s"
        execute_sql(query, [produto_id])
        return redirect('listar_produtos')

    query = "SELECT id, nome, status, custo, marca, linha, unidade, valor FROM loja_produto"
    produtos = execute_sql(query)
    return render(request, 'loja/produtos.html', {'produtos': produtos})

# CRUD para ListaPedidos
def listar_listapedidos(request):
    if request.method == 'POST':
        listapedidos_id = request.POST.get('listapedidos_id')

        if listapedidos_id:  # Edição
            query = "UPDATE loja_listapedidos SET id=%s WHERE id=%s"
            params = (listapedidos_id, listapedidos_id)
        else:  # Criação
            query = "INSERT INTO loja_listapedidos DEFAULT VALUES"
            params = None

        execute_sql(query, params)
        return redirect('listar_listapedidos')

    if 'delete' in request.GET:
        listapedidos_id = request.GET.get('delete')
        query = "DELETE FROM loja_listapedidos WHERE id=%s"
        execute_sql(query, [listapedidos_id])
        return redirect('listar_listapedidos')

    query = "SELECT id FROM loja_listapedidos"
    listapedidos = execute_sql(query)
    return render(request, 'loja/listapedidos.html', {'listapedidos': listapedidos})

def homepage(request):
    return render(request, 'loja/homepage.html')
