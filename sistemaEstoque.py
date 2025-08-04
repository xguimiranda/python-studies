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

while True:
    try:
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
            print("Opção invalida.")
            continue

        if selecao == 1:
            print("--- ADICIONAR PRODUTO ---")
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade inicial: "))
            preco = float(input("Preço unitário (R$): "))
            
            produto = adicionar_produto(nome, qtd, preco)
            print(f"Produto '{produto['nome']}' adicionado com sucesso!")
            print(f"ID: {produto['id']}")
            
        elif selecao == 2:
            print("--- CONSULTA DE ESTOQUE ---\n"
                    "1. Ver todos os produtos\n"
                    "2. Buscar produto específico")
            selecao2 = int(input("Escolha: "))
            if selecao2 not in (1,2):
                print("Opção invalida")
                continue
            if selecao2 == 1:
                print(estoque)

        elif selecao == 6:
            print("Obrigado por usar o sistema de estoque!")
            break

    except ValueError:
        print("Por favor digite apenas numeros validos")
        continue



