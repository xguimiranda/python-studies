# Iteradores e Generators em Python - Notas de Estudo
# -----------------------------------------------------
# Conceitos relacionados que facilitam muito a vida comparado ao Java!

# ==================== ITERADORES ====================
# Um iterador é um objeto que implementa os métodos __iter__() e __next__().
# Ele permite percorrer elementos de uma coleção (como listas, tuplas, etc.) um por vez.

# Exemplo básico usando uma lista:
lista = [1, 2, 3, 4]

# Obtendo o iterador da lista usando a função iter()
iterador = iter(lista)  # Cria um objeto iterador

# O método next() retorna o próximo elemento do iterador
print("=== ITERADOR BÁSICO ===")
print(next(iterador))  # Saída: 1
print(next(iterador))  # Saída: 2
print(next(iterador))  # Saída: 3
print(next(iterador))  # Saída: 4

# Se tentar chamar next() além do último elemento, ocorre uma exceção StopIteration
try:
    print(next(iterador))
except StopIteration:
    print("Fim do iterador!")  # Saída: Fim do iterador!

# Podemos criar nosso próprio iterador implementando os métodos __iter__ e __next__:
class ContadorRegressivo:
    def __init__(self, inicio):
        self.atual = inicio

    def __iter__(self):
        # Retorna o próprio objeto como iterador
        return self

    def __next__(self):
        # Retorna o próximo valor ou levanta StopIteration
        if self.atual <= 0:
            raise StopIteration
        valor = self.atual
        self.atual -= 1
        return valor

# Usando o iterador personalizado:
print("\n=== ITERADOR PERSONALIZADO ===")
for numero in ContadorRegressivo(5):
    print(numero)  # Saída: 5, 4, 3, 2, 1


# ==================== GENERATORS ====================
# Generators são uma forma MUITO mais simples de criar iteradores!
# Usa a palavra-chave 'yield' ao invés de 'return'

def contador_regressivo_generator(inicio):
    """Generator function - muito mais simples que classe iteradora!"""
    atual = inicio
    while atual > 0:
        yield atual  # 'yield' pausa a função e retorna o valor
        atual -= 1   # Quando next() é chamado, continua daqui

print("\n=== GENERATOR FUNCTION ===")
for numero in contador_regressivo_generator(5):
    print(numero)  # Mesmo resultado, código muito mais simples!

# Generator Expression (como list comprehension, mas lazy)
print("\n=== GENERATOR EXPRESSION ===")
quadrados_gen = (x**2 for x in range(5))  # Note os () ao invés de []
print(f"Tipo: {type(quadrados_gen)}")     # <class 'generator'>

for quadrado in quadrados_gen:
    print(quadrado)  # 0, 1, 4, 9, 16

# DIFERENÇA CRUCIAL: Generators são LAZY (preguiçosos)
# Lista normal (carrega tudo na memória):
lista_grande = [x**2 for x in range(1000000)]  # Usa muita memória!

# Generator (calcula sob demanda):
gen_grande = (x**2 for x in range(1000000))     # Usa pouca memória!

print(f"\nMemória - Lista: ~{lista_grande.__sizeof__()} bytes")
# print(f"Memória - Generator: ~{gen_grande.gi_frame.__sizeof__()} bytes")

# EXEMPLOS PRÁTICOS MUITO ÚTEIS:

def ler_arquivo_grande(nome_arquivo):
    """Generator para ler arquivos grandes linha por linha"""
    # Simula leitura de arquivo gigante sem carregar tudo na memória
    for i in range(1000000):  # Simula 1 milhão de linhas
        yield f"Linha {i}: dados importantes aqui..."

def numeros_fibonacci():
    """Generator infinito de números de Fibonacci"""
    a, b = 0, 1
    while True:  # Generator infinito!
        yield a
        a, b = b, a + b

print("\n=== FIBONACCI GENERATOR (primeiros 10) ===")
fib = numeros_fibonacci()
for i in range(10):  # Pega apenas os primeiros 10
    print(next(fib))

def numeros_pares(maximo):
    """Generator com lógica condicional"""
    numero = 0
    while numero <= maximo:
        if numero % 2 == 0:
            yield numero
        numero += 1

print("\n=== NÚMEROS PARES ATÉ 10 ===")
for par in numeros_pares(10):
    print(par)

# PIPELINE DE GENERATORS (muito poderoso!)
def numeros(maximo):
    for i in range(maximo):
        yield i

def apenas_pares(numeros_gen):
    for num in numeros_gen:
        if num % 2 == 0:
            yield num

def ao_quadrado(numeros_gen):
    for num in numeros_gen:
        yield num ** 2

print("\n=== PIPELINE DE GENERATORS ===")
# Combina múltiplos generators em pipeline
pipeline = ao_quadrado(apenas_pares(numeros(10)))
resultado = list(pipeline)  # [0, 4, 16, 36, 64]
print(f"Resultado pipeline: {resultado}")

# MÉTODOS ÚTEIS DE GENERATORS:
gen = (x for x in range(5))

# send() - envia valor para o generator
def contador_com_input():
    contador = 0
    while True:
        valor_recebido = yield contador
        if valor_recebido is not None:
            contador = valor_recebido
        else:
            contador += 1

print("\n=== GENERATOR COM SEND ===")
gen_input = contador_com_input()
print(next(gen_input))      # 0
print(next(gen_input))      # 1
print(gen_input.send(10))   # 10 (reseta contador)
print(next(gen_input))      # 11

# COMPARAÇÃO Java vs Python:
# Java (verboso, complexo):
# class ContadorIterator implements Iterator<Integer> {
#     private int atual;
#     public boolean hasNext() { return atual > 0; }
#     public Integer next() { return atual--; }
# }

# Python Generator (simples):
def contador_simples(inicio):
    while inicio > 0:
        yield inicio
        inicio -= 1

# QUANDO USAR:
# ✅ Iterador customizado: Use generator function
# ✅ Processamento de dados grandes: Use generators (memória eficiente)
# ✅ Sequências infinitas: Use generators
# ✅ Pipeline de transformações: Use generators
# ❌ Acesso aleatório aos dados: Use lista normal

# RESUMO:
# - iter(objeto): retorna um iterador do objeto
# - next(iterador): retorna o próximo elemento ou levanta StopIteration
# - yield: cria um generator (iterator preguiçoso)
# - for ... in ...: usa iteradores internamente para percorrer coleções
# - Generators são iteradores mais simples e eficientes em memória
