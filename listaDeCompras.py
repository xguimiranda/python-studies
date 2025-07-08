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
