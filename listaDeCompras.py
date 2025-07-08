import os

lista = []

while True:
    print("Selecione uma opção:")
    selecao = input("[i]nserir [a]pagar [l]istar: ")

    if selecao not in ('i', 'a', 'l'):
        print("selecione uma opção valida")
        continue
    
    if selecao == 'a':
        indice = input("selecione um indice para apagar: ")
        if not indice.isdigit():
            print("Digite um numero válido!")
            continue
        indice = int(indice)
        if indice not in range(len(lista)):
            print("Não foi possivel apagar esse indice!")
            continue
        else:
            lista.pop(indice)
            os.system('cls')
