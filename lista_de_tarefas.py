#Lista de tarefas

print()
print('Bem-Vindo ao contrutor de lista de tarefas!')
print()


def adiciona(lista):
    print()
    tarefa = input('Digite a tarefa a ser adicionada: ')
    lista.append(tarefa)
    print(f'tarefa "{tarefa}" adicionada com sucesso!')
    print()
    while True:
        print('Opção(1) - Adicionar nova tarefa')
        print('Opção(2) - Voltar ao menu')
        opcao2 = input('Digite uma opção(Apenas números): ')
        if opcao2 == '1':
            print()
            tarefa = input('Digite a tarefa a ser adicionada: ')
            lista.append(tarefa)
            print(f'tarefa "{tarefa}" adicionada com sucesso!')
            print()
        elif opcao2 == '2':
            print()
            break
        else:
            print()
            print('Por favor digite uma opção válida!')
            print()


def mostra(lista):
    print()
    print('Tarefas:')
    for i, j in enumerate(lista):
        print(f'{i+1} - {j}')
    print()


def desfaz(tarefas, retirados):
    try:
        print()
        tamanho_tarefas = len(tarefas)
        retirados.append(tarefas[tamanho_tarefas - 1])
        tarefas.pop()
        print('Ultima ação desfeita com sucesso!')
        print()
    except:
        print('Não ha oq desfazer')
        print('Por favor digite uma opção válida!')
        print()


def refaz(tarefas, retirados):
    try:
        print()
        tamanho_retirados = len(retirados)
        tarefas.append(retirados[tamanho_retirados - 1])
        retirados.pop()
        print('Ação refeita com sucesso!')
        print()
    except:
        print('Não ha oq refazer')
        print('Por favor digite uma opção válida!')
        print()


tarefas = []
retirados = []

while True:
    print('Opção(1) - Adicionar tarefa')
    print('Opção(2) - Lista de tarefas')
    print('Opção(3) - Desfazer ação')
    print('Opção(4) - Refazer ação')
    print('Opção(5) - Sair')
    opcao = input('Digite uma opção(Apenas números): ')

    if opcao == '1':
        adiciona(tarefas)

    elif opcao == '2':
        mostra(tarefas)

    elif opcao == '3':
        desfaz(tarefas, retirados)

    elif opcao == '4':
        refaz(tarefas, retirados)

    elif opcao == '5':
        print()
        print('Saindo... :)')
        break

    else:
        print()
        print('Por favor digite uma opção válida!')
        print()
        continue
