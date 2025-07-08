lista = ["Maria", "João", "Guilherme"]
i = 0

for nome in lista:
    print(i,":", nome)
    i += 1

lista2 = lista.copy()
indices = range(len(lista2))
for indice in indices:
    print(indice, lista[indice])