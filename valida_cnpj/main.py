import funcoes

print('Bem Vindo ao Validador de CNPJ')
cnpj = input('Digite o CNPJ: ')

if funcoes.valida(cnpj):
    print(f'O CNPJ {cnpj} é válido')
else:
    print(f'O CNPJ {cnpj} não é válido')
