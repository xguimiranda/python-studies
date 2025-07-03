from tracemalloc import stop


def calculadora():


    while True:
        try:
            print("=== CALCULADORA SIMPLES ===")
            print("1. Adição (+)")
            print("2. Subtração (-)")
            print("3. Multiplicação (*)")
            print("4. Divisão (/) \n")
            escolha = int(input("Escolha uma operação (1-4): "))

            if escolha == 1:
                numero1 = float(input("Digite o primeiro numero: "))
                numero2 = float(input("Digite o segundo valor: "))
                print(f"Resultado: {numero1} + {numero2} = {numero1+numero2}")

            if escolha == 2:
                numero1 = float(input("Digite o primeiro numero: "))
                numero2 = float(input("Digite o segundo valor: "))
                print(f"Resultado: {numero1} - {numero2} = {numero1-numero2}")

            if escolha == 3:
                numero1 = float(input("Digite o primeiro numero: "))
                numero2 = float(input("Digite o segundo valor: "))
                print(f"Resultado: {numero1} * {numero2} = {numero1*numero2}")

            if escolha == 4:
                numero1 = int(input("Digite o primeiro numero: "))
                numero2 = int(input("Digite o segundo valor: "))
                if(numero2 == 0):
                    print("Error: Divisão com 0")
                    break
                else:
                    print(f"Resultado: {numero1} / {numero2} = {numero1/numero2}")

        except ValueError:
            print("Digite um numero valido!")
            break

    resposta = str(input("Deseja fazer outra operação? (s/n): "))
    if resposta == 'n':
        print("Obrigado por usar a calculadora!")
        stop()

if __name__ == "__main__":
    calculadora()
