import os

estoque = {}
proximo_id = 1

def adicionar_produto(nome, quantidade, preco):
    """Adiciona um produto ao estoque"""
    global proximo_id
    produto = {
        'id': proximo_id,
        'nome': nome,
        'quantidade': quantidade,
        'preco': preco
    }
    estoque[proximo_id] = produto
    proximo_id += 1
    return produto

def buscar_produto_por_nome(nome):
    """Busca um produto pelo nome"""
    for produto in estoque.values():
        if produto['nome'].lower() == nome.lower():
            return produto
    return None

def mostrar_todos_produtos():
    """Mostra todos os produtos formatados"""
    if not estoque:
        print("Nenhum produto cadastrado!")
        return
    
    print("ID | PRODUTO                | QUANTIDADE | PREÇO UNIT. | VALOR TOTAL")
    print("-" * 70)
    for produto in estoque.values():
        valor_total = produto['quantidade'] * produto['preco']
        print(f"{produto['id']:<2} | {produto['nome']:<22} | {produto['quantidade']:<10} | R$ {produto['preco']:<8.2f} | R$ {valor_total:.2f}")

def atualizar_quantidade(nome, tipo_operacao, quantidade):
    """Atualiza quantidade de um produto"""
    produto = buscar_produto_por_nome(nome)
    if not produto:
        return False, "Produto não encontrado!"
    
    if tipo_operacao == 1:  # Entrada
        produto['quantidade'] += quantidade
        return True, f"Entrada realizada! Estoque atual: {produto['quantidade']} unidades"
    else:  # Saída
        if produto['quantidade'] < quantidade:
            return False, f"Estoque insuficiente! Disponível: {produto['quantidade']} unidades"
        produto['quantidade'] -= quantidade
        return True, f"Saída realizada! Estoque atual: {produto['quantidade']} unidades"

def calcular_valor_total_estoque():
    """Calcula o valor total de todo o estoque"""
    total = 0
    for produto in estoque.values():
        total += produto['quantidade'] * produto['preco']
    return total

def produtos_em_falta():
    """Retorna produtos com estoque baixo (≤ 5)"""
    produtos_baixo_estoque = []
    for produto in estoque.values():
        if produto['quantidade'] <= 5:
            produtos_baixo_estoque.append(produto)
    return produtos_baixo_estoque

while True:
    try:
        os.system('cls')
        print(
            "=== SISTEMA DE CONTROLE DE ESTOQUE ===\n" 
            "1. Adicionar produto\n" 
            "2. Consultar estoque\n" 
            "3. Atualizar quantidade\n" 
            "4. Valor total do estoque\n" 
            "5. Produtos em falta\n" 
            "6. Sair\n" 
            )
        selecao = int(input("Escolha uma opção: "))
        if selecao not in [1,2,3,4,5,6]:
            print("Opção inválida.")
            input("Pressione Enter para continuar...")
            continue

        if selecao == 1:
            print("--- ADICIONAR PRODUTO ---")
            nome = input("Nome do produto: ")
            
            # Verificar se produto já existe
            if buscar_produto_por_nome(nome):
                print("Produto já existe! Use a opção 'Atualizar quantidade' para adicionar mais unidades.")
                input("Pressione Enter para continuar...")
                continue
                
            qtd = int(input("Quantidade inicial: "))
            preco = float(input("Preço unitário (R$): "))
            
            produto = adicionar_produto(nome, qtd, preco)
            print(f"Produto '{produto['nome']}' adicionado com sucesso!")
            print(f"ID: {produto['id']}")
            input("Pressione Enter para continuar...")
            
        elif selecao == 2:
            print("--- CONSULTA DE ESTOQUE ---")
            print("1. Ver todos os produtos")
            print("2. Buscar produto específico")
            selecao2 = int(input("Escolha: "))
            
            if selecao2 not in [1,2]:
                print("Opção inválida")
                input("Pressione Enter para continuar...")
                continue
                
            if selecao2 == 1:
                mostrar_todos_produtos()
            else:
                nome_busca = input("Digite o nome do produto: ")
                produto = buscar_produto_por_nome(nome_busca)
                if produto:
                    print("\nProduto encontrado:")
                    print("ID | PRODUTO                | QUANTIDADE | PREÇO UNIT. | VALOR TOTAL")
                    print("-" * 70)
                    valor_total = produto['quantidade'] * produto['preco']
                    print(f"{produto['id']:<2} | {produto['nome']:<22} | {produto['quantidade']:<10} | R$ {produto['preco']:<8.2f} | R$ {valor_total:.2f}")
                else:
                    print("Produto não encontrado!")
            
            input("Pressione Enter para continuar...")

        elif selecao == 3:
            print("--- ATUALIZAR QUANTIDADE ---")
            nome = input("Nome do produto: ")
            
            produto = buscar_produto_por_nome(nome)
            if not produto:
                print("Produto não encontrado!")
                input("Pressione Enter para continuar...")
                continue
            
            print(f"Produto: {produto['nome']}")
            print(f"Estoque atual: {produto['quantidade']} unidades")
            print("1. Entrada (adicionar ao estoque)")
            print("2. Saída (remover do estoque)")
            
            tipo_operacao = int(input("Tipo de movimentação: "))
            if tipo_operacao not in [1, 2]:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")
                continue
            
            quantidade = int(input("Quantidade: "))
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero!")
                input("Pressione Enter para continuar...")
                continue
            
            sucesso, mensagem = atualizar_quantidade(nome, tipo_operacao, quantidade)
            print(mensagem)
            input("Pressione Enter para continuar...")

        elif selecao == 4:
            print("--- VALOR TOTAL DO ESTOQUE ---")
            valor_total = calcular_valor_total_estoque()
            print(f"Valor total do estoque: R$ {valor_total:.2f}")
            
            if estoque:
                print("\nDetalhamento por produto:")
                for produto in estoque.values():
                    valor_produto = produto['quantidade'] * produto['preco']
                    print(f"• {produto['nome']}: {produto['quantidade']} unidades × R$ {produto['preco']:.2f} = R$ {valor_produto:.2f}")
            
            input("Pressione Enter para continuar...")

        elif selecao == 5:
            print("--- PRODUTOS EM FALTA ---")
            produtos_baixo = produtos_em_falta()
            
            if produtos_baixo:
                print("⚠️  Os seguintes produtos estão com estoque baixo (≤ 5):")
                for produto in produtos_baixo:
                    if produto['quantidade'] == 0:
                        print(f"❌ {produto['nome']}: ESGOTADO")
                    else:
                        print(f"⚠️  {produto['nome']}: {produto['quantidade']} unidades")
            else:
                print("✅ Todos os produtos estão com estoque adequado!")
            
            input("Pressione Enter para continuar...")

        elif selecao == 6:
            print("Obrigado por usar o sistema de estoque!")
            break

    except ValueError:
        print("Por favor, digite apenas números válidos!")
        input("Pressione Enter para continuar...")
        continue
    except Exception as e:
        print(f"Erro inesperado: {e}")
        input("Pressione Enter para continuar...")
        continue



