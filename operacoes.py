def soma(v1, v2):
    return v1 + v2

def subtracao(v1, v2):
    return v1 - v2

def multiplica(v1, v2):
    return v1 * v2

def divisao(v1, v2):
    try:
        if v2 == 0:
            raise ZeroDivisionError('Divisão por zero')
        else:
            return v1 / v2
       
    except ZeroDivisionError as ZeroErro:
        return f'Erro: {ZeroErro}'