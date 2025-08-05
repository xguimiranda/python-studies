# Unpacking (Desempacotamento) em Python - Guia Fácil
# ----------------------------------------------------
# Este conceito NÃO EXISTE no Java! É uma das features mais poderosas do Python.

# UNPACKING BÁSICO - Extrair valores de sequências
coordenadas = (10, 20)
x, y = coordenadas  # Desempacota a tupla
print(f"x: {x}, y: {y}")  # x: 10, y: 20

# Com listas também funciona
dados = ['João', 25, 'Programador']
nome, idade, profissao = dados
print(f"Nome: {nome}, Idade: {idade}, Profissão: {profissao}")

# UNPACKING COM * (ASTERISCO) - Pega "o resto"
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pegar primeiro, último e o resto
primeiro, *meio, ultimo = numeros
print(f"Primeiro: {primeiro}")    # 1
print(f"Meio: {meio}")            # [2, 3, 4, 5, 6, 7, 8, 9]
print(f"Último: {ultimo}")        # 10

# Pegar primeiros elementos e ignorar o resto
a, b, c, *resto = numeros
print(f"a: {a}, b: {b}, c: {c}")  # a: 1, b: 2, c: 3
print(f"resto: {resto}")          # [4, 5, 6, 7, 8, 9, 10]

# UNPACKING EM FUNÇÕES - Passar argumentos
def calcular(a, b, c):
    return a + b + c

valores = [10, 20, 30]
resultado = calcular(*valores)    # Equivale a calcular(10, 20, 30)
print(f"Resultado: {resultado}")  # 60

# UNPACKING DE DICIONÁRIOS com **
def apresentar_pessoa(nome, idade, cidade):
    return f"{nome}, {idade} anos, mora em {cidade}"

dados_pessoa = {'nome': 'Ana', 'idade': 28, 'cidade': 'São Paulo'}
apresentacao = apresentar_pessoa(**dados_pessoa)
print(f"Apresentação: {apresentacao}")

# SWAP (TROCA) DE VARIÁVEIS - Super simples!
# Java: temp = a; a = b; b = temp;
# Python: uma linha só!
a = 10
b = 20
print(f"Antes: a={a}, b={b}")
a, b = b, a  # Troca em uma linha!
print(f"Depois: a={a}, b={b}")

# MÚLTIPLOS RETORNOS DE FUNÇÃO
def dividir_com_resto(dividendo, divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto  # Retorna tupla

q, r = dividir_com_resto(17, 5)  # Desempacota o retorno
print(f"17 ÷ 5 = {q} resto {r}")

# UNPACKING EM LOOPS - Muito útil!
pessoas = [
    ('João', 25),
    ('Maria', 30),
    ('Pedro', 35)
]

for nome, idade in pessoas:  # Desempacota cada tupla
    print(f"{nome} tem {idade} anos")

# Com dicionários
estoque = {'mouse': 50, 'teclado': 150, 'monitor': 800}
for produto, preco in estoque.items():  # .items() retorna tuplas (chave, valor)
    print(f"{produto}: R$ {preco}")

# UNPACKING COM ENUMERATE
lista_compras = ['Pão', 'Leite', 'Ovos', 'Queijo']
for indice, item in enumerate(lista_compras):  # enumerate retorna (índice, valor)
    print(f"{indice + 1}. {item}")

# IGNORAR VALORES COM _ (UNDERSCORE)
dados_completos = ('João', 'Silva', 25, 'Programador', 'São Paulo')
nome, sobrenome, _, profissao, _ = dados_completos  # Ignora idade e cidade
print(f"Profissional: {nome} {sobrenome}, {profissao}")

# NESTED UNPACKING - Desempacotamento aninhado
dados_pessoa = ('João', ('São Paulo', 'SP'), (11, 987654321))
nome, (cidade, estado), (ddd, telefone) = dados_pessoa
print(f"{nome} - {cidade}/{estado} - ({ddd}) {telefone}")

# CASOS PRÁTICOS MUITO ÚTEIS:

# 1. Ler arquivo CSV e processar
def processar_linha_csv(linha):
    nome, idade, salario = linha.strip().split(',')
    return nome, int(idade), float(salario)

linha_exemplo = "João,30,5000.50"
nome, idade, salario = processar_linha_csv(linha_exemplo)
print(f"Processado: {nome}, {idade} anos, R$ {salario}")

# 2. Unpacking para validação de entrada
def validar_coordenadas(coordenadas):
    try:
        x, y = coordenadas
        return isinstance(x, (int, float)) and isinstance(y, (int, float))
    except ValueError:
        return False

print(f"Coordenadas válidas: {validar_coordenadas((10, 20))}")   # True
print(f"Coordenadas inválidas: {validar_coordenadas((10,))}")    # False

# 3. Unpacking em compreensões
pontos = [(1, 2), (3, 4), (5, 6)]
distancias = [x**2 + y**2 for x, y in pontos]  # Desempacota dentro da comprehension
print(f"Distâncias: {distancias}")

# RESUMO - Por que é poderoso:
# ✅ Código mais limpo e legível
# ✅ Menos variáveis temporárias
# ✅ Trabalhar com estruturas de dados de forma natural
# ✅ Múltiplos retornos sem criar classes
# ✅ Processamento de dados mais elegante

print("\n🚀 Unpacking é uma das features que faz Python ser tão elegante!")
