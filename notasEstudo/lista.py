"""
Listas em Python (tipo list)
- São mutáveis: você pode alterar os valores depois de criar.
- Aceitam vários tipos de dados (int, str, float, etc).
- Cada valor tem um índice (posição), começando do zero.

Principais operações:
    - Criar: lista = [valor1, valor2, ...]
    - Ler: lista[indice]
    - Alterar: lista[indice] = novo_valor
    - Apagar: del lista[indice] ou lista.pop(indice)
    - Adicionar: lista.append(valor) ou lista.insert(indice, valor)
    - Limpar: lista.clear()
    - Juntar: lista.extend([valores]) ou lista1 + lista2

Exemplo prático:
"""

# Criando uma lista
lista = [10, 20, 30, 40]  # índices: 0   1   2   3

# Adicionando valores
lista.append(50)           # Adiciona 50 no final
lista.append(60)
lista.insert(1, 15)        # Insere 15 na posição 1

# Removendo valores
removido = lista.pop()     # Remove o último valor (60)
removido2 = lista.pop(2)   # Remove o valor no índice 2 (30)

# Alterando valores
lista[0] = 5               # Altera o valor do índice 0 para 5

# Lendo valores
print('Valor na posição 1:', lista[1])

# Exibindo a lista final e valores removidos
print('Lista final:', lista)
print('Valores removidos:', removido, removido2)

"""
Resumo dos métodos mais usados:
- append(valor): adiciona no final
- insert(indice, valor): insere na posição escolhida
- pop(indice): remove e retorna o valor da posição (sem índice, remove o último)
- del lista[indice]: apaga o valor da posição
- clear(): remove todos os valores
- extend([valores]): adiciona vários valores
- +: junta listas

Dica: Use sempre índices para acessar ou alterar valores.
"""