palavra = 'violao'
chances = 3
tentativas = []
print('Bem vindo ao jogo de adivinhação')
print(f'A palavra a ser adivinhada possui {len(palavra)}({"*" * len(palavra)}) caracteres')
print
while True:
    if chances == 0:
        print('Que pena, acabaram suas chances :(')
        break

    tentativa = input(f'Digite uma letra(você tem {chances} chances): ')

    if len(tentativa) > 1:
        print('Por favor digite apenas 1 letra')
        continue
    elif tentativa.isdigit():
        print('Por favor digite apenas letras')
        continue

    if tentativa in palavra:
        print(f'Muito bem, a letra {tentativa} está na palavra')
        tentativas.append(tentativa)
    else:
        print(f'Que pena, a letra {tentativa} não existe na palavra')
        chances -= 1


    palavra_aux = ''
    for i in palavra:
        if i in tentativas:
            palavra_aux += i
        else:
            palavra_aux += '*'

    if palavra_aux == palavra:
        print(f'Parabéns, você ganhou!!! A palavra era {palavra_aux}.')
        break
    else:
        print(f'A palavra está assim {palavra_aux}')