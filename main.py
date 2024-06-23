"""
Crie uma calculadora simples que pode realizar operações básicas como adição, subtração, multiplicação e divisão.
"""

"""def soma(v1, v2):
    return v1 + v2

def subtracao(v1, v2):
    return v1 - v2

def multiplica(v1, v2):
    return v1 * v2

def divisao(v1, v2):
    try:
        if v2 != 0:
            return v1 / v2
        else:
            raise ZeroDivisionError('Divisão por zero')
    except ZeroDivisionError as ZeroErro:
        return f'Erro: {ZeroErro}'
        
while True:
    operadores = ['+', '-', '/', '*']
    operacao = input('Informe o simbolo correspondente para cada operação (+, -, /, *): ')
    try:
        if operacao not in operadores:
            raise ValueError('Operador não correspondente')
        else:
            break
    except ValueError as e:
        print(f'Erro: {e}')
        continue

while True:
    valor1 = float(input('Informe o primeiro valor: '))
    valor2 = float(input('Informe o segundo valor: '))

    try:
        if valor1 and valor2 is not float:
            raise TypeError('Digite apenas numeros')
        else:
            break
    except TypeError as erro:
        print(f'Erro: {erro}')
        continue

if operacao == '+':
    res_soma = soma(valor1, valor2)
    print(f'Soma: {res_soma}')
elif operacao == '-':
    res_subtracao = subtracao(valor1, valor2)
    print(f'Subtração: {res_subtracao}')
elif operacao == '/':
    res_divisao = divisao(valor1, valor2)
    print(f'Divisão: {res_divisao}')
elif operacao == '*':
    res_multiplica = multiplica(valor1, valor2)
    print(f'Multiplicação: {res_multiplica}')

"""