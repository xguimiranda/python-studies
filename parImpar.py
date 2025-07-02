def verificar_par_impar():
    print("=== VERIFICADOR DE PAR OU ÍMPAR ===")
    print("Digite números para verificar se são pares ou ímpares")
    print("Digite 0 para sair do programa\n")

    while True:
        try:

            numero = int(input("Digite um número (0 para sair): "))

            if numero == 0:
                print("Programa encerrado. Obrigado!")
                break

            if numero % 2 == 0:
                print(f"O número {numero} é PAR\n")
            else:
                print(f"O número {numero} é ÍMPAR\n")

        except ValueError:
            print("Por favor, digite apenas números inteiros!\n")

if __name__ == "__main__":
    verificar_par_impar()
