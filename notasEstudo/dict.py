# Dicionários em Python: Métodos e Exemplos Simples

# O que é um dicionário?
# É uma estrutura que armazena pares de chave:valor.
# Exemplo:
pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}

# Métodos úteis dos dicionários:

# 1. len(dicionario) - Conta quantas chaves existem
print('Quantidade de chaves:', len(pessoa))  # 2

# 2. keys() - Retorna todas as chaves
print('Chaves:', list(pessoa.keys()))  # ['nome', 'sobrenome']

# 3. values() - Retorna todos os valores
print('Valores:', list(pessoa.values()))  # ['Luiz', 'Miranda']

# 4. items() - Retorna pares (chave, valor)
print('Itens:', list(pessoa.items()))  # [('nome', 'Luiz'), ('sobrenome', 'Miranda')]

# 5. get(chave, valor_padrao) - Busca valor pela chave, retorna valor_padrao se não existir
print('Nome:', pessoa.get('nome', 'Não existe'))  # Luiz
print('Idade:', pessoa.get('idade', 'Não existe'))  # Não existe

# 6. setdefault(chave, valor) - Adiciona chave com valor se não existir
# pessoa.setdefault('idade', 30)
print('Com idade:', pessoa)  # {'nome': 'Luiz', 'sobrenome': 'Miranda', 'idade': 30}

# 7. copy() - Cria uma cópia rasa do dicionário
copia = pessoa.copy()
print('Cópia:', copia)

# 8. pop(chave) - Remove item pela chave e retorna o valor removido
nome_removido = pessoa.pop('nome')
print('Nome removido:', nome_removido)
print('Após pop:', pessoa)

# 9. popitem() - Remove o último item adicionado (Python 3.7+)
ultimo = pessoa.popitem()
print('Último removido:', ultimo)
print('Após popitem:', pessoa)

# 10. update() - Atualiza o dicionário com outro dicionário, lista de pares ou argumentos nomeados
# Usando outro dicionário:
# pessoa.update({'nome': 'Ana', 'idade': 25})
print('Atualizado com dict:', pessoa)

# Usando lista de listas (par chave/valor):
lista_pares = [['nome', 'Carlos'], ['sobrenome', 'Silva']]
# pessoa.update(lista_pares)
print('Atualizado com lista:', pessoa)

# Usando argumentos nomeados:
pessoa.update(nome='João', cidade='São Paulo')
print('Atualizado com kwargs:', pessoa)

# Dica: Para acessar um valor, use pessoa['chave'] ou pessoa.get('chave')
# Para evitar erro se a chave não existir, prefira pessoa.get('chave', valor_padrao)
