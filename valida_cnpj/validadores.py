def valida(cnpj):
    if sequencia(cnpj):
        return False
    try:
        novo_cnpj = limpa_cnpj(cnpj)[:12]
        novo_cnpj += primeiro_digito(novo_cnpj)
        novo_cnpj += segundo_digito(novo_cnpj)
    except Exception as e:
        return False

    if novo_cnpj == limpa_cnpj(cnpj):
        return True
    else:
        return False


def sequencia(cnpj):
    seq = cnpj[0] * len(cnpj)
    if seq == limpa_cnpj(cnpj):
        return True
    else:
        return False


def limpa_cnpj(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


def primeiro_digito(cnpj):
    cnpj_lista = [int(i) for i in cnpj]
    l1 = [i for i in range(5, 1, -1)]
    l2 = [i for i in range(9, 1, -1)]

    p1 = sum([(cnpj_lista[i] * l1[i]) for i in range(4)])
    p2 = sum([(cnpj_lista[i + 4] * l2[i]) for i in range(8)])

    p3 = p1 + p2

    if 11 - (p3 % 11) > 9:
        return '0'
    else:
        return str(11 - (p3 % 11))


def segundo_digito(cnpj):
    cnpj_lista = [int(i) for i in cnpj]
    l1 = [i for i in range(6, 1, -1)]
    l2 = [i for i in range(9, 1, -1)]

    p1 = sum([(cnpj_lista[i] * l1[i]) for i in range(5)])
    p2 = sum([(cnpj_lista[i + 5] * l2[i]) for i in range(8)])

    p3 = p1 + p2

    if 11 - (p3 % 11) > 9:
        return '0'
    else:
        return str(11 - (p3 % 11))
