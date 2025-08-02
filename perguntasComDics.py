# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print("pergunta:",pergunta['Pergunta'])
    print()

    opções = pergunta['Opções']
    for i, opção in enumerate(opções):
        print(f'{i})', opção)
    print()

    escolha = input("Escolha uma opção: ")

    acertou = False
    escolha_int = None
    qtd_opções = len(opções)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opções:
            if opções[escolha_int] == pergunta['Resposta']:
                acertou == True

    if acertou:
        qtd_acertos += 1
        print("acertou👍")
    else:
        print("Errou❌")


    print()