import re
import sys

print("***TESTE DE CPF***")#746.824.890-70
entrada = input("Digite um cpf: ")
cpf_envidado = re.sub(r'[^0-9]', '', entrada)
# cpf_envidado.replace('.', '').replace('-', '').replace(' ', '') maneira mais simples

entrada_repetida = entrada == entrada[0] * len(entrada)
if entrada_repetida:
    print("Você mandou CPF invalido!")
    sys.exit()

nove_digitos = cpf_envidado[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = ((resultado_digito_1 * 10) % 11) 
digito_1 = digito_1 if digito_1 <= 9 else 0

contador_regressivo_2 = 11
resultado_digito_2 = 0

for digito in nove_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
resultado_digito_2 += int(digito_1) * 2

digito_2 = ((resultado_digito_2 * 10) % 11) 
digito_2 = digito_2 if digito_2 <= 9 else 0

calculated_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_envidado == calculated_cpf:
    print(f"{cpf_envidado} é valido!")
else:
    print("Cpf invalido!")