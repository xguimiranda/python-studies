import os

lista = []

while True:
    print("Selecione uma opção:")
    selecao = input("[i]nserir [a]pagar [l]istar [s]air: ")

    if selecao not in ('i', 'a', 'l', 's'):
        print("selecione uma opção valida")
        continue
    
    if selecao == 'a':
        try:
            indice = int(input("selecione um indice para apagar: "))
            del lista[indice]
            os.system('cls')
        except (ValueError):
            print("Digite um numero valido!")
        except IndexError:
            print("Numero não existe na lista")
        except Exception:
            print("Error Desconhecido")

    if selecao == 'i':
        os.system('cls')
        item = input("Produto: ")
        lista.append(item)

    if selecao == 'l':
        os.system('cls')
        for indice, nome in enumerate(lista):
            print(indice, nome)

    if selecao == 's':
        print("Obrigado, volte sempre!")
        break
