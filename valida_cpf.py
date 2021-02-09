# Validar o cpf

indices = []
cpf_soma = 0
contador = 10
digito2 = 0

while True:
    cpf = input('Digite seu cpf(apenas números): ')
    if not cpf.isdigit():
        print('Por favor digite apenas números!')
        continue
    elif len(cpf) != 11:
        print('O CPF deve conter 11 dígitos!')
        continue
    else:
        break

#Digito 1

for i in range(9):
    indice = int(cpf[i])
    indices.append(indice)

for i in range(9):
    cpf_soma = cpf_soma + indices[i] * contador
    contador -= 1

identificador = 11 - (cpf_soma % 11)

if identificador > 9:
    digito1 = 0
else:
    digito1 = identificador

print(f'O primeiro digito é: {digito1}')

indices.append(digito1)

#Digito 2

contador = 11
cpf_soma = 0

for i in range(10):
    cpf_soma = cpf_soma + indices[i] * contador
    contador -= 1

identificador = 11 - (cpf_soma % 11)

if identificador > 9:
    digito2 = 0
else:
    digito2 = identificador

print(f'O segundo digito é: {digito2}')

indices.append(digito2)

novo_cpf = ''
for i in indices:
    indice = str(i)
    novo_cpf = novo_cpf+indice

if cpf == novo_cpf:
    print('CPF válido')
else:
    print('CPF inválido')
