# Funções Lambda e Higher-Order Functions - Guia Fácil
# ------------------------------------------------------
# Lambdas são funções anônimas de uma linha. Higher-order functions são funções
# que recebem ou retornam outras funções. Muito mais poderoso que Java!

# ==================== LAMBDA BÁSICO ====================
# Função normal:
def quadrado(x):
    return x ** 2

# Mesma função como lambda:
quadrado_lambda = lambda x: x ** 2

print("=== LAMBDA BÁSICO ===")
print(f"Função normal: {quadrado(5)}")        # 25
print(f"Lambda: {quadrado_lambda(5)}")        # 25

# Lambda com múltiplos parâmetros:
somar = lambda a, b: a + b
multiplicar = lambda x, y, z: x * y * z

print(f"Soma: {somar(3, 7)}")                # 10
print(f"Multiplicação: {multiplicar(2, 3, 4)}")  # 24

# ==================== MAP() - Aplica função a todos elementos ====================
numeros = [1, 2, 3, 4, 5]

# Com função normal:
quadrados = list(map(quadrado, numeros))
print(f"\n=== MAP COM FUNÇÃO ===")
print(f"Quadrados: {quadrados}")  # [1, 4, 9, 16, 25]

# Com lambda (mais conciso):
quadrados_lambda = list(map(lambda x: x ** 2, numeros))
print(f"Quadrados (lambda): {quadrados_lambda}")

# Exemplos práticos com map:
nomes = ['joão', 'maria', 'pedro']
nomes_formatados = list(map(lambda nome: nome.title(), nomes))
print(f"Nomes formatados: {nomes_formatados}")  # ['João', 'Maria', 'Pedro']

precos = [10.0, 25.50, 99.99]
precos_com_desconto = list(map(lambda p: p * 0.9, precos))
print(f"Preços com 10% desconto: {precos_com_desconto}")

# ==================== FILTER() - Filtra elementos ====================
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filtrar números pares:
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"\n=== FILTER ===")
print(f"Números pares: {pares}")  # [2, 4, 6, 8, 10]

# Filtrar números maiores que 5:
maiores_que_5 = list(filter(lambda x: x > 5, numeros))
print(f"Maiores que 5: {maiores_que_5}")  # [6, 7, 8, 9, 10]

# Exemplo prático: filtrar produtos caros
produtos = [
    {'nome': 'Mouse', 'preco': 50},
    {'nome': 'Teclado', 'preco': 150},
    {'nome': 'Monitor', 'preco': 800},
    {'nome': 'Cabo', 'preco': 20}
]

produtos_caros = list(filter(lambda p: p['preco'] > 100, produtos))
print(f"Produtos caros: {produtos_caros}")

# ==================== REDUCE() - Reduz lista a um valor ====================
from functools import reduce

numeros = [1, 2, 3, 4, 5]

# Somar todos os números:
soma = reduce(lambda a, b: a + b, numeros)
print(f"\n=== REDUCE ===")
print(f"Soma: {soma}")  # 15

# Encontrar o maior número:
maior = reduce(lambda a, b: a if a > b else b, numeros)
print(f"Maior: {maior}")  # 5

# Exemplo prático: concatenar strings
palavras = ['Python', 'é', 'muito', 'legal']
frase = reduce(lambda a, b: a + ' ' + b, palavras)
print(f"Frase: {frase}")  # "Python é muito legal"

# ==================== SORTED() COM KEY ====================
pessoas = [
    {'nome': 'João', 'idade': 30},
    {'nome': 'Maria', 'idade': 25},
    {'nome': 'Pedro', 'idade': 35}
]

print(f"\n=== SORTED COM LAMBDA ===")
# Ordenar por idade:
por_idade = sorted(pessoas, key=lambda p: p['idade'])
print("Por idade:", [p['nome'] for p in por_idade])  # ['Maria', 'João', 'Pedro']

# Ordenar por nome:
por_nome = sorted(pessoas, key=lambda p: p['nome'])
print("Por nome:", [p['nome'] for p in por_nome])    # ['João', 'Maria', 'Pedro']

# Exemplo com strings - ordenar por tamanho:
palavras = ['Python', 'Java', 'JavaScript', 'C++', 'Go']
por_tamanho = sorted(palavras, key=lambda palavra: len(palavra))
print(f"Por tamanho: {por_tamanho}")  # ['Go', 'C++', 'Java', 'Python', 'JavaScript']

# ==================== FUNÇÕES QUE RETORNAM FUNÇÕES ====================
def criar_multiplicador(fator):
    """Retorna uma função que multiplica por um fator"""
    return lambda x: x * fator

# Criando diferentes multiplicadores:
dobrar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
multiplicar_por_10 = criar_multiplicador(10)

print(f"\n=== FUNÇÕES QUE RETORNAM FUNÇÕES ===")
print(f"Dobrar 5: {dobrar(5)}")                    # 10
print(f"Triplicar 4: {triplicar(4)}")              # 12
print(f"Multiplicar 7 por 10: {multiplicar_por_10(7)}")  # 70

# ==================== COMBINANDO TUDO ====================
# Exemplo prático: processar vendas

vendas = [
    {'produto': 'Notebook', 'quantidade': 2, 'preco_unitario': 2500},
    {'produto': 'Mouse', 'quantidade': 5, 'preco_unitario': 50},
    {'produto': 'Teclado', 'quantidade': 3, 'preco_unitario': 150},
    {'produto': 'Monitor', 'quantidade': 1, 'preco_unitario': 800}
]

print(f"\n=== PROCESSAMENTO DE VENDAS ===")

# 1. Calcular valor total de cada venda
vendas_com_total = list(map(
    lambda v: {**v, 'total': v['quantidade'] * v['preco_unitario']}, 
    vendas
))

for venda in vendas_com_total:
    print(f"{venda['produto']}: {venda['quantidade']}x R${venda['preco_unitario']} = R${venda['total']}")

# 2. Filtrar vendas acima de R$ 200
vendas_altas = list(filter(lambda v: v['total'] > 200, vendas_com_total))
print(f"\nVendas acima de R$ 200: {len(vendas_altas)} vendas")

# 3. Calcular faturamento total
faturamento_total = reduce(lambda acc, v: acc + v['total'], vendas_com_total, 0)
print(f"Faturamento total: R$ {faturamento_total}")

# 4. Produto mais vendido (por quantidade)
produto_top = max(vendas, key=lambda v: v['quantidade'])
print(f"Produto mais vendido: {produto_top['produto']} ({produto_top['quantidade']} unidades)")

# ==================== ANY() E ALL() COM LAMBDA ====================
numeros = [2, 4, 6, 8, 10]

print(f"\n=== ANY E ALL ===")
# Verificar se todos são pares:
todos_pares = all(map(lambda x: x % 2 == 0, numeros))
print(f"Todos são pares: {todos_pares}")  # True

# Verificar se algum é maior que 5:
algum_maior_5 = any(map(lambda x: x > 5, numeros))
print(f"Algum maior que 5: {algum_maior_5}")  # True

# ==================== ENUMERATE() COM LAMBDA ====================
frutas = ['maçã', 'banana', 'laranja', 'uva']

# Criar dicionário com índices:
frutas_indexadas = dict(map(lambda item: (item[1], item[0]), enumerate(frutas)))
print(f"\n=== ENUMERATE COM LAMBDA ===")
print(f"Frutas indexadas: {frutas_indexadas}")  # {'maçã': 0, 'banana': 1, ...}

# ==================== LAMBDA COM IF/ELSE (TERNÁRIO) ====================
# Classificar números como par ou ímpar:
classificar = lambda x: 'par' if x % 2 == 0 else 'ímpar'

numeros = [1, 2, 3, 4, 5]
classificacoes = list(map(classificar, numeros))
print(f"\n=== LAMBDA COM IF/ELSE ===")
print(f"Classificações: {classificacoes}")  # ['ímpar', 'par', 'ímpar', 'par', 'ímpar']

# Aplicar desconto baseado na quantidade:
aplicar_desconto = lambda preco, qtd: preco * 0.9 if qtd > 10 else preco
print(f"Preço com desconto: R$ {aplicar_desconto(100, 15)}")  # R$ 90.0
print(f"Preço sem desconto: R$ {aplicar_desconto(100, 5)}")   # R$ 100

# ==================== QUANDO USAR E QUANDO NÃO USAR ====================

# ✅ BOM - Operações simples e claras:
quadrados_bom = list(map(lambda x: x**2, [1, 2, 3, 4]))

# ❌ RUIM - Lógica complexa (use função normal):
# complicado = lambda x: x**2 if x > 0 else -x**2 if x < -10 else 0

# ✅ MELHOR - Função normal para lógica complexa:
def processar_numero(x):
    if x > 0:
        return x**2
    elif x < -10:
        return -x**2
    else:
        return 0

# ==================== CLOSURES COM LAMBDA ====================
def criar_contador(inicial=0):
    """Closure que mantém estado"""
    contador = [inicial]  # Lista para ser mutável
    
    return {
        'incrementar': lambda: contador.__setitem__(0, contador[0] + 1) or contador[0],
        'decrementar': lambda: contador.__setitem__(0, contador[0] - 1) or contador[0],
        'valor': lambda: contador[0]
    }

print(f"\n=== CLOSURES COM LAMBDA ===")
contador = criar_contador(10)
print(f"Valor inicial: {contador['valor']()}")      # 10
print(f"Incrementar: {contador['incrementar']()}")   # 11
print(f"Incrementar: {contador['incrementar']()}")   # 12
print(f"Decrementar: {contador['decrementar']()}")   # 11

# RESUMO:
# ✅ Lambdas são ótimas para operações simples de uma linha
# ✅ map(), filter(), reduce() são muito poderosas com lambdas
# ✅ sorted() com key=lambda é muito útil
# ✅ Higher-order functions deixam código mais funcional e elegante
# ❌ Evite lambdas complexas - use funções normais
# ✅ Combinação de map/filter/reduce pode substituir muitos loops
