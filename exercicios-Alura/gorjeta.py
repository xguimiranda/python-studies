def calculaGorjeta(valorConta, gorjeta):
    if valorConta < 0 or gorjeta < 0:
        print("Os valorem não podem ser negativos!")
        return
    valorGorjeta = valorConta * (gorjeta/100)
    valorFinal = valorGorjeta + valorConta
    print(f"Valor da gorjeta: R${valorGorjeta:.2f}")
    print(f"Valor total a pagar: R${valorFinal:.2f}")

try:
    valorConta = float(input("Valor da conta: R$ "))
    percGorjeta = int(input("Porcentagem da gorjeta (10, 15, 20): "))
    calculaGorjeta(valorConta, percGorjeta)
except ValueError:
    print("Digite apenas Numeros!")
