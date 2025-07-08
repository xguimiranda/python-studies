lista = ["Maria", "João", "Guilherme"]
i = 0

for nome in lista:
    print(i,":", nome)
    i += 1

lista2 = lista.copy()
indices = range(len(lista2))
for indice in indices:
    print(indice, lista[indice])

lista3 = lista.copy()
lista_enumerada = enumerate(lista3)

for itens in lista_enumerada: #pode usar apenas uma vez
    print(itens)

for indice, nome in enumerate(lista3): # reutilizavel e mais organizado
    print(indice, nome)
