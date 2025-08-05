# Context Managers (with statements) em Python - Guia Fácil
# -----------------------------------------------------------
# Context Managers garantem que recursos sejam abertos e fechados corretamente.
# O 'with' é muito mais seguro que try/finally do Java!

import os
from contextlib import contextmanager

# ==================== CONCEITO BÁSICO ====================
# No Java você faria:
# try {
#     File file = new File("arquivo.txt");
#     // usar arquivo
# } finally {
#     file.close();  // Pode esquecer!
# }

# Em Python com 'with':
print("=== ABERTURA DE ARQUIVO SEGURA ===")
# Cria arquivo para exemplo
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Olá, mundo!")
    # Arquivo é fechado automaticamente quando sai do 'with'

# Lendo o arquivo
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(f"Conteúdo: {conteudo}")

# O arquivo está garantidamente fechado aqui, mesmo se houver erro!

# ==================== CONTEXT MANAGER CUSTOMIZADO ====================
class GerenciadorDeArquivo:
    """Context manager customizado para demonstração"""
    
    def __init__(self, nome_arquivo, modo):
        self.nome_arquivo = nome_arquivo
        self.modo = modo
        self.arquivo = None
    
    def __enter__(self):
        """Chamado quando entra no 'with'"""
        print(f"🔓 Abrindo arquivo: {self.nome_arquivo}")
        self.arquivo = open(self.nome_arquivo, self.modo)
        return self.arquivo
    
    def __exit__(self, tipo_exc, valor_exc, traceback):
        """Chamado quando sai do 'with' (sempre!)"""
        print(f"🔒 Fechando arquivo: {self.nome_arquivo}")
        if self.arquivo:
            self.arquivo.close()
        
        # Se retornar True, suprime exceções
        # Se retornar False/None, propaga exceções
        if tipo_exc:
            print(f"❌ Erro ocorreu: {tipo_exc.__name__}: {valor_exc}")
        return False  # Não suprimir exceções

print("\n=== CONTEXT MANAGER CUSTOMIZADO ===")
with GerenciadorDeArquivo('teste.txt', 'w') as f:
    f.write("Teste de context manager")
    # Mesmo se der erro aqui, o arquivo será fechado

# ==================== USANDO @contextmanager ====================
@contextmanager
def cronometro():
    """Context manager para medir tempo usando decorator"""
    import time
    print("⏱️  Iniciando cronômetro...")
    inicio = time.time()
    try:
        yield  # O código do 'with' executa aqui
    finally:
        fim = time.time()
        print(f"⏱️  Tempo decorrido: {fim - inicio:.4f} segundos")

print("\n=== CONTEXT MANAGER COM DECORATOR ===")
with cronometro():
    import time
    time.sleep(0.1)  # Simula operação que demora
    print("Fazendo algo que demora...")

# ==================== MÚLTIPLOS CONTEXT MANAGERS ====================
print("\n=== MÚLTIPLOS CONTEXT MANAGERS ===")
# Pode usar múltiplos 'with' em uma linha
with open('arquivo1.txt', 'w') as f1, open('arquivo2.txt', 'w') as f2:
    f1.write("Conteúdo arquivo 1")
    f2.write("Conteúdo arquivo 2")
    # Ambos arquivos fechados automaticamente

# ==================== CONTEXT MANAGER PARA CONEXÃO BD ====================
class ConexaoBancoDados:
    """Simula uma conexão com banco de dados"""
    
    def __init__(self, host, usuario):
        self.host = host
        self.usuario = usuario
        self.conectado = False
    
    def __enter__(self):
        print(f"🔌 Conectando ao banco: {self.host} como {self.usuario}")
        self.conectado = True
        return self
    
    def __exit__(self, tipo_exc, valor_exc, traceback):
        print(f"🔌 Desconectando do banco: {self.host}")
        self.conectado = False
        if tipo_exc:
            print(f"❌ Erro na transação: {valor_exc}")
            print("🔄 Fazendo rollback...")
        else:
            print("✅ Commit realizado com sucesso")
    
    def executar_query(self, sql):
        if not self.conectado:
            raise Exception("Não conectado ao banco!")
        print(f"📝 Executando: {sql}")
        return f"Resultado de: {sql}"

print("\n=== CONTEXT MANAGER PARA BANCO ===")
with ConexaoBancoDados("localhost", "admin") as db:
    resultado = db.executar_query("SELECT * FROM usuarios")
    print(f"Resultado: {resultado}")

# ==================== CONTEXT MANAGER PARA ESTADO TEMPORÁRIO ====================
@contextmanager
def estado_temporario(objeto, atributo, valor_temporario):
    """Muda um atributo temporariamente e restaura depois"""
    valor_original = getattr(objeto, atributo)
    setattr(objeto, atributo, valor_temporario)
    print(f"🔄 {atributo}: {valor_original} → {valor_temporario}")
    try:
        yield objeto
    finally:
        setattr(objeto, atributo, valor_original)
        print(f"🔄 {atributo}: {valor_temporario} → {valor_original}")

class Configuracao:
    def __init__(self):
        self.debug = False
        self.timeout = 30

config = Configuracao()
print(f"\n=== ESTADO TEMPORÁRIO ===")
print(f"Debug inicial: {config.debug}")

with estado_temporario(config, 'debug', True):
    print(f"Debug durante 'with': {config.debug}")
    # Fazer algo que precisa de debug

print(f"Debug final: {config.debug}")

# ==================== CONTEXT MANAGER PARA DIRETÓRIO ====================
@contextmanager
def mudar_diretorio(novo_dir):
    """Muda diretório temporariamente"""
    dir_original = os.getcwd()
    print(f"📂 Mudando de {dir_original} para {novo_dir}")
    try:
        os.chdir(novo_dir)
        yield novo_dir
    finally:
        os.chdir(dir_original)
        print(f"📂 Voltando para {dir_original}")

# Exemplo (comentado para não causar erro se diretório não existir)
# with mudar_diretorio('/tmp'):
#     print(f"Diretório atual: {os.getcwd()}")
#     # Fazer operações no diretório temporário

# ==================== CONTEXT MANAGER PARA SUPRESSÃO DE EXCEÇÕES ====================
from contextlib import suppress

print("\n=== SUPRESSÃO DE EXCEÇÕES ===")
# Em vez de try/except verbose:
try:
    int("abc")  # Vai dar erro
except ValueError:
    pass  # Ignora o erro

# Com suppress (mais limpo):
with suppress(ValueError):
    int("abc")  # Erro é ignorado automaticamente
    print("Esta linha não executa")

print("Continuou normalmente após erro suprimido")

# ==================== CONTEXT MANAGER PARA CAPTURA DE SAÍDA ====================
from io import StringIO
import sys

@contextmanager
def capturar_stdout():
    """Captura prints para processar depois"""
    stdout_original = sys.stdout
    stdout_capturado = StringIO()
    sys.stdout = stdout_capturado
    try:
        yield stdout_capturado
    finally:
        sys.stdout = stdout_original

print("\n=== CAPTURA DE SAÍDA ===")
with capturar_stdout() as saida:
    print("Esta mensagem será capturada")
    print("Esta também")

conteudo_capturado = saida.getvalue()
print(f"Capturado: '{conteudo_capturado.strip()}'")

# ==================== CASOS PRÁTICOS ÚTEIS ====================

@contextmanager
def loading_spinner(mensagem="Carregando..."):
    """Simula loading spinner"""
    import threading
    import time
    
    parar = False
    
    def spinner():
        chars = "|/-\\"
        i = 0
        while not parar:
            print(f"\r{mensagem} {chars[i % len(chars)]}", end="", flush=True)
            time.sleep(0.1)
            i += 1
        print(f"\r{mensagem} ✅")
    
    thread = threading.Thread(target=spinner)
    thread.start()
    
    try:
        yield
    finally:
        parar = True
        thread.join()

# Exemplo de uso (comentado para não atrapalhar output)
# with loading_spinner("Processando dados..."):
#     time.sleep(2)  # Simula operação demorada

@contextmanager
def log_operacao(nome_operacao):
    """Log início e fim de operações"""
    print(f"🚀 Iniciando: {nome_operacao}")
    inicio = time.time()
    try:
        yield
        status = "✅ SUCESSO"
    except Exception as e:
        status = f"❌ ERRO: {e}"
        raise
    finally:
        fim = time.time()
        duracao = fim - inicio
        print(f"🏁 Finalizando: {nome_operacao} | {status} | {duracao:.2f}s")

print("\n=== LOG DE OPERAÇÃO ===")
with log_operacao("Processamento de dados"):
    time.sleep(0.1)  # Simula processamento
    print("Processando...")

# RESUMO DOS CONTEXT MANAGERS:
# ✅ Garantem limpeza de recursos (arquivos, conexões, etc.)
# ✅ Mais seguro que try/finally manual
# ✅ Código mais limpo e legível
# ✅ Pode ser customizado com __enter__/__exit__ ou @contextmanager
# ✅ Úteis para: arquivos, banco de dados, locks, estado temporário
# ✅ 'with' sempre executa cleanup, mesmo com exceções

# Limpar arquivos de exemplo
import os
for arquivo in ['exemplo.txt', 'teste.txt', 'arquivo1.txt', 'arquivo2.txt']:
    if os.path.exists(arquivo):
        os.remove(arquivo)
