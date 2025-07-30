def multiplicar(multiplicador):
    def tipo_multiplicacao(numero):
        return numero * multiplicador
    return tipo_multiplicacao

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadriplicar = multiplicar(4)

while True:
    print("\nEscolha o tipo de multiplicação:")
    print("1 - Duplicar")
    print("2 - Triplicar")
    print("3 - Quadriplicar")
    print("0 - Sair")
    
