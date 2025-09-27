def validar_cpf(cpf):
    if not cpf.isdigit():
        return "Erro: O CPF deve conter apenas números."
    elif len(cpf) != 11:
        return "Erro: O CPF deve ter exatamente 11 dígitos. "
    else:
        return "CPF Valido"

cpf = input("Digite o seu CPF: ")
print(validar_cpf(cpf))
