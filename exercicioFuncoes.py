
def multiplicacao(*args):
    total = 1
    for numeros in args:
        total *= args
    return total

def ParImpar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print("***TESTE***")
numeros = input("Digite numeros para ser multiplicados: ")
print(multiplicacao(numeros))


numero = input("Digite um numero para ver se é par ou impar: ")
ParImpar(numero)

