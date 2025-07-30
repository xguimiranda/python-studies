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
    try:
        escolha = int(input("Digite a opção desejada: "))
        if escolha == 0:
            print("Saindo...")
            break
        if escolha not in [1, 2, 3]:
            print("Opção inválida. Tente novamente.")
            continue
        numero = float(input("Digite o número para multiplicar: "))
        if escolha == 1:
            resultado = duplicar(numero)
            print(f"Duplicado: {resultado}")
        elif escolha == 2:
            resultado = triplicar(numero)
            print(f"Triplicado: {resultado}")
        elif escolha == 3:
            resultado = quadriplicar(numero)
            print(f"Quadriplicado: {resultado}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")
