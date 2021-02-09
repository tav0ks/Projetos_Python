# Sistema de perguntas e respostas utilizando dicionários

print()

print(f'Interprete as perguntas e escolha uma das respostas em colchetes\n'
      f'(Por favor digite apenas as letras referentes as respostas):')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 5+5?',
        'respostas': {
            'a': '6',
            'b': '2',
            'c': '10',
        },
        'resposta_certa': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 2*2?',
        'respostas': {
            'a': '4',
            'b': '13',
            'c': '8',
        },
        'resposta_certa': 'a'
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 6*3?',
        'respostas': {
            'a': '67',
            'b': '32',
            'c': '18',
        },
        'resposta_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 7+5?',
        'respostas': {
            'a': '16',
            'b': '12',
            'c': '9',
        },
        'resposta_certa': 'b'
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 9-4?',
        'respostas': {
            'a': '8',
            'b': '5',
            'c': '16',
        },
        'resposta_certa': 'b'
    },

}

print()

possiveis_respostas = []
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        possiveis_respostas.append(rk)
        print(f'[{rk}]: {rv}')

    while True:

        resposta_usuario = input('Sua resposta: ')

        if resposta_usuario.isdigit():
            print(f'{resposta_usuario} não é uma resposta válida, por favor tente novamente')
            continue
        if not len(resposta_usuario) == 1:
            print(f'{resposta_usuario} não é uma resposta válida, por favor tente novamente')
            continue
        if resposta_usuario not in possiveis_respostas:
            print(f'{resposta_usuario} não é uma resposta válida, por favor tente novamente')
            continue
        break

    if resposta_usuario == pv['resposta_certa']:
        print('Muito bem, você acertou')
        respostas_certas += 1
    else:
        print('Você errou, tente novamente')

    print()

qnt_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qnt_perguntas * 100

print(f'Você acertou {respostas_certas} pergunta(s).')
print(f'Você obteve {porcentagem_acerto}% de acertos.')
