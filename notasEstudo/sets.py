# Sets (Conjuntos) em Python - Guia Fácil
# ---------------------------------------
# Sets são coleções de elementos únicos, sem ordem e sem índices.
# Muito usados para eliminar duplicados e fazer operações matemáticas de conjuntos.

# Como criar um set:
# - Usando set(iterável)
# - Usando chaves {elementos}
s1 = set('Luiz')         # {'L', 'u', 'i', 'z'}
s2 = set()               # set vazio
s3 = {'Luiz', 1, 2, 3}   # set com vários tipos imutáveis

# Principais características dos sets:
# - Não aceita elementos duplicados
# - Não garante ordem dos elementos
# - Não tem índices (não dá para acessar por posição)
# - Aceita apenas tipos imutáveis (str, int, float, tuple)
# - É iterável (pode usar for, in, not in)

# Exemplo: Remover duplicados de uma lista
lista = [1, 2, 2, 3, 3, 3, 1]
set_sem_duplicados = set(lista)   # {1, 2, 3}
print(set_sem_duplicados)

# Convertendo set para lista (se quiser acessar por índice)
lista_unica = list(set_sem_duplicados)
print(lista_unica)

# Verificando se um elemento está no set
print(3 in set_sem_duplicados)    # True
print(4 not in set_sem_duplicados) # True

# Iterando sobre um set
for elemento in set_sem_duplicados:
    print(elemento)

# Métodos principais dos sets:
s = set()
s.add('Python')                  # Adiciona um elemento
s.add(42)
s.update([1, 2, 3])              # Adiciona vários elementos (iterável)
print(s)
s.discard('Python')              # Remove o elemento se existir (não dá erro)
print(s)
s.clear()                        # Remove todos os elementos
print(s)

# Operações matemáticas com sets:
a = {1, 2, 3}
b = {2, 3, 4}

# União: todos os elementos dos dois sets
print('União:', a | b)           # {1, 2, 3, 4}

# Interseção: elementos presentes nos dois sets
print('Interseção:', a & b)      # {2, 3}

# Diferença: elementos só no primeiro set
print('Diferença:', a - b)       # {1}

# Diferença simétrica: elementos que estão em um ou outro, mas não nos dois
print('Diferença simétrica:', a ^ b) # {1, 4}

# Resumo rápido:
# - Use sets para garantir elementos únicos
# - Ideal para operações matemáticas de conjuntos
# - Não serve para acessar por índice ou manter ordem

# Dica: Se precisar de elementos únicos e ordem, use dict.fromkeys(lista) ou OrderedDict (Python 3.7+ mantém ordem em dict)

# Métodos úteis adicionais:
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Verificar se é subconjunto/superconjunto
print(s1.issubset(s2))        # False - s1 está contido em s2?
print(s1.issuperset(s2))      # False - s1 contém s2?
print({1, 2}.issubset(s1))    # True

# Verificar se são disjuntos (sem elementos em comum)
print(s1.isdisjoint({6, 7}))  # True - não têm elementos em comum

# Diferença usando método (equivale a -)
print(s1.difference(s2))      # {1, 2}

# Casos práticos úteis:
# 1. Encontrar elementos únicos entre duas listas
lista1 = [1, 2, 3, 4]
lista2 = [3, 4, 5, 6]
unicos_lista1 = set(lista1) - set(lista2)  # {1, 2}
print(f"Elementos só na lista1: {unicos_lista1}")

# 2. Verificar se duas listas têm elementos em comum
tem_comum = bool(set(lista1) & set(lista2))  # True
print(f"Listas têm elementos em comum: {tem_comum}")

# 3. Remover duplicados mantendo tipo lista
def remover_duplicados(lista):
    return list(dict.fromkeys(lista))  # Mantém ordem (Python 3.7+)

original = [1, 2, 2, 3, 1, 4]
sem_dup = remover_duplicados(original)  # [1, 2, 3, 4]
print(f"Original: {original}")
print(f"Sem duplicados: {sem_dup}")