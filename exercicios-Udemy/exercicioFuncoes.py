def multiplicacao(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print("***TESTE***")
numeros = input("Digite os números que deseja multiplicar, separados por espaço: ")
numeros_lista = [int(n) for n in numeros.split()]
print("Resultado da multiplicação: ", multiplicacao(*numeros_lista))

numero = int(input("Digite um número para ver se é par ou ímpar: "))
print(par_impar(numero))

