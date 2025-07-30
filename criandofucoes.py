def multiplicar(multiplicador):
    def tipo_multiplicacao(numero):
        return numero * multiplicador
    return tipo_multiplicacao

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadriplicar = multiplicar(4)

print(duplicar(2))
print(triplicar(4))
print(quadriplicar(6))
