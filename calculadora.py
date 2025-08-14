def calculadora():
    while True:
        try:
            print("\n=== CALCULADORA SIMPLES ===")
            print("1. Adição (+)")
            print("2. Subtração (-)")
            print("3. Multiplicação (*)")
            print("4. Divisão (/) \n")
            escolha = int(input("Escolha uma operação (1-4): "))

            if escolha not in [1, 2, 3, 4]:
                print("Opção inválida! Escolha entre 1 e 4.")
                continue

            numero1 = float(input("Digite o primeiro numero: "))
            numero2 = float(input("Digite o segundo numero: "))

            if escolha == 1:
                resultado = numero1 + numero2
                print(f"Resultado: {numero1} + {numero2} = {resultado}")

            elif escolha == 2:
                resultado = numero1 - numero2
                print(f"Resultado: {numero1} - {numero2} = {resultado}")

            elif escolha == 3:
                resultado = numero1 * numero2
                print(f"Resultado: {numero1} * {numero2} = {resultado}")

            elif escolha == 4:
                if numero2 == 0:
                    print("Error: Divisão por zero não é permitida!")
                    continue
                else:
                    resultado = numero1 / numero2
                    print(f"Resultado: {numero1} / {numero2} = {resultado}")

        except ValueError:
            print("Por favor, digite apenas números válidos!")
            continue

        while True:
            resposta = input("\nDeseja fazer outra operação? (s/n): ").lower().strip()
            if resposta in ['s', 'sim']:
                break
            elif resposta in ['n', 'nao', 'não']:
                print("Obrigado por usar a calculadora!")
                return
            else:
                print("Por favor, digite 's' para sim ou 'n' para não.")

if __name__ == "__main__":
    calculadora()
    jiandijan
