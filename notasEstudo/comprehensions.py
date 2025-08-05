# Comprehensions em Python - Guia Fácil
# ----------------------------------------
# Comprehensions são uma forma concisa e pythônica de criar listas, dicts e sets.
# No Java, você faria com loops - aqui é muito mais elegante!

# LIST COMPREHENSION - Criar listas de forma compacta
# Sintaxe: [expressão for item in iterável if condição]

# Exemplo 1: Quadrados dos números de 0 a 9
# Java: for(int i=0; i<10; i++) { lista.add(i*i); }
quadrados = [x**2 for x in range(10)]
print(f"Quadrados: {quadrados}")  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Exemplo 2: Apenas números pares ao quadrado
pares_quadrados = [x**2 for x in range(10) if x % 2 == 0]
print(f"Pares ao quadrado: {pares_quadrados}")  # [0, 4, 16, 36, 64]

# Exemplo 3: Processando strings
nomes = ['João', 'MARIA', 'ana', 'PEDRO']
nomes_formatados = [nome.title() for nome in nomes]
print(f"Nomes formatados: {nomes_formatados}")  # ['João', 'Maria', 'Ana', 'Pedro']

# Exemplo 4: Filtrando e transformando
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Pegar apenas ímpares, multiplicar por 3
impares_x3 = [n * 3 for n in numeros if n % 2 == 1]
print(f"Ímpares × 3: {impares_x3}")  # [3, 9, 15, 21, 27]

# DICT COMPREHENSION - Criar dicionários
# Sintaxe: {chave: valor for item in iterável if condição}

# Exemplo 1: Números e seus quadrados
quadrados_dict = {x: x**2 for x in range(5)}
print(f"Dict quadrados: {quadrados_dict}")  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Exemplo 2: Contagem de caracteres em uma palavra
palavra = "python"
contagem = {char: palavra.count(char) for char in set(palavra)}
print(f"Contagem chars: {contagem}")  # {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

# Exemplo 3: Filtrar dicionário existente
precos = {'notebook': 2500, 'mouse': 50, 'teclado': 200, 'monitor': 800}
caros = {item: preco for item, preco in precos.items() if preco > 100}
print(f"Produtos caros: {caros}")  # {'notebook': 2500, 'teclado': 200, 'monitor': 800}

# SET COMPREHENSION - Criar sets
# Sintaxe: {expressão for item in iterável if condição}

# Exemplo: Primeiras letras únicas de uma lista de palavras
palavras = ['python', 'java', 'javascript', 'php', 'perl']
primeiras_letras = {palavra[0] for palavra in palavras}
print(f"Primeiras letras: {primeiras_letras}")  # {'p', 'j'}

# COMPREHENSIONS ANINHADAS (nested)
# Exemplo: Matriz 3x3
matriz = [[i + j for j in range(3)] for i in range(3)]
print(f"Matriz: {matriz}")  # [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Exemplo prático: Achatar lista de listas
lista_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
achatada = [item for sublista in lista_listas for item in sublista]
print(f"Lista achatada: {achatada}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# QUANDO USAR:
# ✅ Para transformações simples e filtros
# ✅ Quando deixa o código mais legível
# ❌ Evite se a lógica for muito complexa (use loop normal)

# COMPARAÇÃO Java vs Python:
# Java (verbose):
# List<Integer> pares = new ArrayList<>();
# for(int i = 0; i < 10; i++) {
#     if(i % 2 == 0) {
#         pares.add(i * i);
#     }
# }

# Python (conciso):
pares_py = [i**2 for i in range(10) if i % 2 == 0]
print(f"Comparação - pares: {pares_py}")
