# Métodos de String em Python - Guia Fácil
# ------------------------------------------
# Python tem métodos de string muito mais poderosos que Java!

texto = "  Olá, Mundo Python!  "

# LIMPEZA E FORMATAÇÃO (mais simples que Java)
print(f"Original: '{texto}'")
print(f"strip(): '{texto.strip()}'")        # Remove espaços início/fim
print(f"lstrip(): '{texto.lstrip()}'")      # Remove espaços só no início
print(f"rstrip(): '{texto.rstrip()}'")      # Remove espaços só no fim

# CASE CONVERSIONS (mais opções que Java)
nome = "joão da silva"
print(f"title(): {nome.title()}")           # João Da Silva
print(f"capitalize(): {nome.capitalize()}") # João da silva
print(f"swapcase(): {nome.swapcase()}")     # JOÃO DA SILVA

# VERIFICAÇÕES BOOLEANAS (muito úteis!)
email = "user@email.com"
numero = "12345"
alfanum = "abc123"

print(f"isdigit(): {numero.isdigit()}")     # True - só números
print(f"isalpha(): {'abc'.isalpha()}")      # True - só letras
print(f"isalnum(): {alfanum.isalnum()}")    # True - letras e números
print(f"islower(): {'abc'.islower()}")      # True - tudo minúsculo
print(f"isupper(): {'ABC'.isupper()}")     # True - tudo maiúsculo

# BUSCA E SUBSTITUIÇÃO (mais flexível que Java)
frase = "Python é incrível, Python é poderoso"
print(f"count(): {frase.count('Python')}")           # 2 - conta ocorrências
print(f"find(): {frase.find('é')}")                  # 7 - posição da primeira ocorrência
print(f"rfind(): {frase.rfind('Python')}")           # 20 - última ocorrência
print(f"startswith(): {frase.startswith('Python')}") # True
print(f"endswith(): {frase.endswith('poderoso')}")   # True

# REPLACE mais poderoso
print(f"replace(): {frase.replace('Python', 'Java')}")           # Substitui todas
print(f"replace(count=1): {frase.replace('Python', 'Java', 1)}") # Substitui só a primeira

# SPLIT E JOIN (muito usado!)
csv_data = "João,25,São Paulo,Programador"
dados = csv_data.split(',')  # ['João', '25', 'São Paulo', 'Programador']
print(f"split(): {dados}")

# JOIN - o contrário do split (método do separador!)
lista_palavras = ['Python', 'é', 'demais']
frase_junta = ' '.join(lista_palavras)     # "Python é demais"
print(f"join(): {frase_junta}")

# Diferentes separadores
print(f"join com vírgula: {', '.join(dados)}")
print(f"join com hífen: {'-'.join(['a', 'b', 'c'])}")

# FORMATAÇÃO DE STRINGS (f-strings são únicos do Python!)
nome = "Maria"
idade = 30
salario = 5000.50

# F-strings (Python 3.6+) - muito mais limpo que Java
print(f"Nome: {nome}, Idade: {idade}, Salário: R$ {salario:.2f}")

# Formatação de números
pi = 3.14159
print(f"Pi com 2 casas: {pi:.2f}")          # 3.14
print(f"Pi com 4 casas: {pi:.4f}")          # 3.1416
print(f"Percentual: {0.85:.1%}")             # 85.0%

# Alinhamento (padding)
produto = "Mouse"
preco = 50.0
print(f"Produto: {produto:<15} Preço: R$ {preco:>8.2f}")  # Alinha à esquerda/direita

# PARTICIONAMENTO (único do Python!)
email = "usuario@gmail.com"
usuario, arroba, dominio = email.partition('@')
print(f"partition(): usuario='{usuario}', dominio='{dominio}'")

# ENCODING/DECODING (mais simples que Java)
texto_unicode = "Olá, código com acentos!"
texto_bytes = texto_unicode.encode('utf-8')    # Converte para bytes
texto_volta = texto_bytes.decode('utf-8')     # Volta para string
print(f"Encoding funciona: {texto_volta == texto_unicode}")

# MÉTODOS MENOS COMUNS MAS ÚTEIS
print(f"zfill(10): {'123'.zfill(10)}")       # 0000000123 - preenche com zeros
print(f"center(20): {'Python'.center(20, '-')}")  # -------Python-------

# CASOS PRÁTICOS COMUNS:
def validar_cpf_basico(cpf):
    """Validação básica de CPF usando métodos de string"""
    # Remove pontos e hífens
    cpf_limpo = cpf.replace('.', '').replace('-', '')
    # Verifica se tem 11 dígitos
    return cpf_limpo.isdigit() and len(cpf_limpo) == 11

def formatar_telefone(numero):
    """Formata número de telefone"""
    numero_limpo = ''.join(filter(str.isdigit, numero))  # Remove não-números
    if len(numero_limpo) == 11:
        return f"({numero_limpo[:2]}) {numero_limpo[2:7]}-{numero_limpo[7:]}"
    return "Número inválido"

# Testando funções
print(f"CPF válido: {validar_cpf_basico('123.456.789-01')}")
print(f"Telefone formatado: {formatar_telefone('11987654321')}")

# COMPARAÇÃO com Java:
# Java: string.substring(0, 5).toUpperCase().trim()
# Python: string[:5].upper().strip()  - muito mais conciso!
