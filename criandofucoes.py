def multiplicar(multiplicador):
        def tipo_multiplicacao(numero):
            return numero * multiplicador
    return tipo_multiplicacao

    duplicar = multiplicar(2)
    triplicar= multiplicador(3)
    quadriplicar= multiplicador(4)

    print(duplicar(2))
    print(triplicar(4))
    print(quadriplicar(6))
