# Decoradores em Python - Guia Fácil
# ------------------------------------
# Decoradores são funções que modificam/estendem o comportamento de outras funções.
# É como "envolver" uma função com funcionalidade extra - não existe no Java!

import time
from functools import wraps

# ==================== CONCEITO BÁSICO ====================
def meu_decorador(funcao):
    """Decorador básico que adiciona prints antes e depois"""
    def wrapper(*args, **kwargs):
        print("🔸 Antes da execução")
        resultado = funcao(*args, **kwargs)
        print("🔸 Depois da execução")
        return resultado
    return wrapper

# Usando o decorador com @
@meu_decorador
def dizer_ola(nome):
    print(f"Olá, {nome}!")

print("=== DECORADOR BÁSICO ===")
dizer_ola("João")
# Saída:
# 🔸 Antes da execução
# Olá, João!
# 🔸 Depois da execução

# ==================== DECORADOR DE TEMPO ====================
def cronometrar(funcao):
    """Mede o tempo de execução de uma função"""
    @wraps(funcao)  # Preserva metadados da função original
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f"⏱️  {funcao.__name__} executou em {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

@cronometrar
def operacao_lenta():
    """Simula uma operação que demora"""
    time.sleep(0.1)  # Simula 100ms de processamento
    return "Operação concluída"

print("\n=== DECORADOR DE TEMPO ===")
resultado = operacao_lenta()
print(f"Resultado: {resultado}")

# ==================== DECORADOR COM PARÂMETROS ====================
def repetir(vezes):
    """Decorador que repete a execução de uma função"""
    def decorador(funcao):
        @wraps(funcao)
        def wrapper(*args, **kwargs):
            for i in range(vezes):
                print(f"Execução {i+1}:")
                resultado = funcao(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def cumprimentar(nome):
    print(f"Oi, {nome}! 👋")

print("\n=== DECORADOR COM PARÂMETROS ===")
cumprimentar("Maria")

# ==================== DECORADOR DE CACHE ====================
def cache_simples(funcao):
    """Cache simples para evitar recalcular resultados"""
    cache = {}
    
    @wraps(funcao)
    def wrapper(*args):
        if args in cache:
            print(f"📁 Cache hit para {args}")
            return cache[args]
        
        print(f"🔄 Calculando para {args}")
        resultado = funcao(*args)
        cache[args] = resultado
        return resultado
    return wrapper

@cache_simples
def fibonacci(n):
    """Fibonacci com cache para ser mais eficiente"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("\n=== DECORADOR DE CACHE ===")
print(f"fibonacci(10) = {fibonacci(10)}")
print(f"fibonacci(10) novamente = {fibonacci(10)}")  # Usa cache

# ==================== DECORADORES MÚLTIPLOS ====================
def bold(funcao):
    """Adiciona negrito (simulado)"""
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return f"**{resultado}**"
    return wrapper

def italic(funcao):
    """Adiciona itálico (simulado)"""
    @wraps(funcao)
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        return f"*{resultado}*"
    return wrapper

@bold
@italic  # Aplicados de baixo para cima: italic(bold(texto))
def texto_formatado(mensagem):
    return mensagem

print("\n=== DECORADORES MÚLTIPLOS ===")
print(texto_formatado("Texto importante"))  # **_Texto importante_**

# ==================== DECORADORES DE CLASSE ====================
def singleton(cls):
    """Padrão Singleton usando decorador"""
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Configuracao:
    def __init__(self):
        self.dados = {}
        print("🏗️  Criando instância de Configuração")

print("\n=== DECORADOR DE CLASSE (SINGLETON) ===")
config1 = Configuracao()
config2 = Configuracao()
print(f"São a mesma instância: {config1 is config2}")  # True

# ==================== DECORADORES BUILT-IN ÚTEIS ====================

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
    
    @property  # Transforma método em atributo
    def nome(self):
        return self._nome.title()
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter  # Permite modificar o preço com validação
    def preco(self, valor):
        if valor < 0:
            raise ValueError("Preço não pode ser negativo")
        self._preco = valor
    
    @staticmethod  # Método que não precisa de instância
    def validar_codigo(codigo):
        return len(codigo) == 8 and codigo.isdigit()
    
    @classmethod  # Método que recebe a classe como primeiro argumento
    def criar_produto_padrao(cls):
        return cls("Produto Genérico", 0.0)

print("\n=== DECORADORES BUILT-IN ===")
produto = Produto("notebook gamer", 2500.0)
print(f"Nome formatado: {produto.nome}")  # @property
produto.preco = 3000.0  # @setter
print(f"Novo preço: {produto.preco}")

print(f"Código válido: {Produto.validar_codigo('12345678')}")  # @staticmethod
produto_padrao = Produto.criar_produto_padrao()  # @classmethod
print(f"Produto padrão: {produto_padrao.nome}")

# ==================== CASOS PRÁTICOS ====================

def validar_tipos(**tipos):
    """Decorador para validar tipos de argumentos"""
    def decorador(funcao):
        @wraps(funcao)
        def wrapper(*args, **kwargs):
            # Validar argumentos posicionais
            import inspect
            sig = inspect.signature(funcao)
            params = list(sig.parameters.keys())
            
            for i, arg in enumerate(args):
                if i < len(params):
                    param_name = params[i]
                    if param_name in tipos:
                        if not isinstance(arg, tipos[param_name]):
                            raise TypeError(f"{param_name} deve ser {tipos[param_name].__name__}")
            
            return funcao(*args, **kwargs)
        return wrapper
    return decorador

@validar_tipos(nome=str, idade=int)
def criar_pessoa(nome, idade):
    return f"Pessoa: {nome}, {idade} anos"

print("\n=== VALIDAÇÃO DE TIPOS ===")
try:
    print(criar_pessoa("João", 30))      # ✅ OK
    print(criar_pessoa("Maria", "25"))   # ❌ Erro: idade deve ser int
except TypeError as e:
    print(f"Erro: {e}")

# ==================== DECORATOR PARA RETRY ====================
def retry(max_tentativas=3):
    """Repete função em caso de erro"""
    def decorador(funcao):
        @wraps(funcao)
        def wrapper(*args, **kwargs):
            for tentativa in range(max_tentativas):
                try:
                    return funcao(*args, **kwargs)
                except Exception as e:
                    print(f"Tentativa {tentativa + 1} falhou: {e}")
                    if tentativa == max_tentativas - 1:
                        raise
            return None
        return wrapper
    return decorador

@retry(max_tentativas=3)
def operacao_instavel():
    import random
    if random.random() < 0.7:  # 70% chance de falhar
        raise Exception("Operação falhou")
    return "Sucesso!"

print("\n=== DECORADOR RETRY ===")
try:
    resultado = operacao_instavel()
    print(f"Resultado: {resultado}")
except Exception as e:
    print(f"Falhou após todas as tentativas: {e}")

# RESUMO:
# ✅ Decoradores adicionam funcionalidade sem modificar o código original
# ✅ @property, @staticmethod, @classmethod são muito úteis
# ✅ Podem ser empilhados (múltiplos decoradores)
# ✅ Úteis para: logging, cache, validação, retry, autenticação
# ✅ Deixam o código mais limpo e reutilizável
