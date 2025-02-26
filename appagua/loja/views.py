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

# View para listar, adicionar e remover produtos contidos em uma lista de pedidos
def listar_produtos_contidos(request):
    if request.method == 'POST':
        id_lista_pedidos = request.POST.get('id_lista_pedidos')
        id_produto = request.POST.get('id_produto')
        valor = request.POST.get('valor')
        quantidade = request.POST.get('quantidade')

        if id_lista_pedidos and id_produto and valor and quantidade:
            query = """
                INSERT INTO loja_produtoscontidos (id_lista_pedidos_id, id_produto_id, valor, quantidade)
                VALUES (%s, %s, %s, %s)
            """
            params = (id_lista_pedidos, id_produto, valor, quantidade)
            execute_sql(query, params)

        return redirect('listar_produtos_contidos')

    if 'delete' in request.GET:
        produto_id = request.GET.get('delete')
        lista_id = request.GET.get('lista_id')

        query = """
            DELETE FROM loja_produtoscontidos 
            WHERE id_lista_pedidos_id = %s AND id_produto_id = %s
        """
        execute_sql(query, [lista_id, produto_id])
        return redirect('listar_produtos_contidos')

    query = """
        SELECT pc.id_lista_pedidos_id, pc.id_produto_id, p.nome, pc.valor, pc.quantidade 
        FROM loja_produtoscontidos pc
        JOIN loja_produto p ON pc.id_produto_id = p.id
        ORDER BY pc.id_lista_pedidos_id, p.nome
    """
    produtos_contidos = execute_sql(query)

    # Buscar todas as listas de pedidos para exibição no formulário
    query_listas = "SELECT id FROM loja_listapedidos"
    listas_pedidos = execute_sql(query_listas)

    # Buscar todos os produtos para exibição no formulário
    query_produtos = "SELECT id, nome FROM loja_produto"
    produtos = execute_sql(query_produtos)

    return render(request, 'loja/produtos_contidos.html', {
        'produtos_contidos': produtos_contidos,
        'listas_pedidos': listas_pedidos,
        'produtos': produtos
    })

# View para listar, adicionar, editar e remover pedidos
def listar_pedidos(request):
    pedido_edit = None  # Para armazenar o pedido a ser editado
    filtros = []
    params = []

    # Capturar filtros da URL (GET)
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    status = request.GET.get('status')
    id_cliente = request.GET.get('id_cliente')
    id_entregador = request.GET.get('id_entregador')

    # Construindo a query base com JOINs necessários
    query = """
        SELECT p.id, p.data_solicitacao, p.hora_solicitacao, p.valor_total, p.status,
               c.nome AS cliente, e.nome AS entregador, l.id AS lista_pedidos, cp.id AS cupom
        FROM loja_pedido p
        JOIN loja_cliente c ON p.id_cliente_id = c.id
        JOIN loja_entregador e ON p.id_entregador_id = e.id
        JOIN loja_listapedidos l ON p.id_lista_pedidos_id = l.id
        LEFT JOIN loja_cupom cp ON p.id_cupom_id = cp.id
    """

    # Aplicando filtros dinamicamente
    if data_inicio:
        filtros.append("p.data_solicitacao >= %s")
        params.append(data_inicio)
    
    if data_fim:
        filtros.append("p.data_solicitacao <= %s")
        params.append(data_fim)

    if status:
        filtros.append("p.status = %s")
        params.append(status)

    if id_cliente:
        filtros.append("p.id_cliente_id = %s")
        params.append(id_cliente)

    if id_entregador:
        filtros.append("p.id_entregador_id = %s")
        params.append(id_entregador)

    # Se houver filtros, adiciona o WHERE na query
    if filtros:
        query += " WHERE " + " AND ".join(filtros)

    query += " ORDER BY p.data_solicitacao DESC, p.hora_solicitacao DESC"

    pedidos = execute_sql(query, params)

    if request.method == 'POST':
        pedido_id = request.POST.get('pedido_id')
        data_solicitacao = request.POST.get('data_solicitacao')
        hora_solicitacao = request.POST.get('hora_solicitacao')
        status = request.POST.get('status')
        id_cliente = request.POST.get('id_cliente')
        id_entregador = request.POST.get('id_entregador')
        id_cupom = request.POST.get('id_cupom') or None
        id_lista_pedidos = request.POST.get('id_lista_pedidos')

        # Recalcular o valor total com base nos produtos na lista de pedidos
        query_total = """
            SELECT SUM(pc.valor * pc.quantidade) AS valor_total
            FROM loja_produtoscontidos pc
            WHERE pc.id_lista_pedidos_id = %s
        """
        resultado = execute_sql(query_total, [id_lista_pedidos])
        valor_total = resultado[0]['valor_total'] if resultado and resultado[0]['valor_total'] else 0.00

        if pedido_id:  # Se o ID existe, EDITAR pedido
            query = """
                UPDATE loja_pedido 
                SET data_solicitacao=%s, 
                    hora_solicitacao=%s, 
                    valor_total=%s, 
                    status=%s, 
                    id_cliente_id=%s, 
                    id_entregador_id=%s, 
                    id_cupom_id=%s, 
                    id_lista_pedidos_id=%s
                WHERE id=%s
            """
            params = (data_solicitacao, hora_solicitacao, valor_total, status, 
                      id_cliente, id_entregador, id_cupom, id_lista_pedidos, pedido_id)
            execute_sql(query, params)
        else:  # Se o ID **NÃO** existe, CRIAR pedido
            query = """
                INSERT INTO loja_pedido (data_solicitacao, hora_solicitacao, valor_total, status, 
                                         id_cliente_id, id_entregador_id, id_cupom_id, id_lista_pedidos_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (data_solicitacao, hora_solicitacao, valor_total, status, 
                      id_cliente, id_entregador, id_cupom, id_lista_pedidos)
            execute_sql(query, params)

        return redirect('listar_pedidos')

    if 'delete' in request.GET:  # Excluir pedido
        pedido_id = request.GET.get('delete')
        query = "DELETE FROM loja_pedido WHERE id=%s"
        execute_sql(query, [pedido_id])
        return redirect('listar_pedidos')

    if 'edit' in request.GET:  # Editar pedido (Preencher formulário)
        pedido_id = request.GET.get('edit')
        query = """
            SELECT id, data_solicitacao, hora_solicitacao, valor_total, status, 
                   id_cliente_id, id_entregador_id, id_lista_pedidos_id, id_cupom_id 
            FROM loja_pedido WHERE id=%s
        """
        pedido_edit = execute_sql(query, [pedido_id])
        if pedido_edit:
            pedido_edit = pedido_edit[0]  # Pegamos o primeiro resultado da lista

            # Calcular o valor total baseado nos produtos da lista de pedidos
            query_total = """
                SELECT SUM(pc.valor * pc.quantidade) AS valor_total
                FROM loja_produtoscontidos pc
                WHERE pc.id_lista_pedidos_id = %s
            """
            resultado = execute_sql(query_total, [pedido_edit['id_lista_pedidos_id']])
            pedido_edit['valor_total'] = resultado[0]['valor_total'] if resultado and resultado[0]['valor_total'] else 0.00

    # Buscar opções para dropdowns
    clientes = execute_sql("SELECT id, nome FROM loja_cliente")
    entregadores = execute_sql("SELECT id, nome FROM loja_entregador")
    listas_pedidos = execute_sql("SELECT id FROM loja_listapedidos")
    cupons = execute_sql("SELECT id FROM loja_cupom")

    return render(request, 'loja/pedidos.html', {
        'pedidos': pedidos,
        'clientes': clientes,
        'entregadores': entregadores,
        'listas_pedidos': listas_pedidos,
        'cupons': cupons,
        'pedido_edit': pedido_edit  # Passando o pedido a ser editado para o template
    })


def homepage(request):
    return render(request, 'loja/homepage.html')
