from operadores import operacao
from operacoes import soma, subtracao, divisao, multiplica

valor1 = float(input('Informe o primeiro valor: '))
valor2 = float(input('Informe o segundo valor: '))

if operacao == '+':
    res_soma = soma(valor1, valor2)
    print(f'{res_soma:.0f}')

elif operacao == '-':
    res_subtracao = subtracao(valor1, valor2)
    print(f'{res_subtracao:.0f}')

elif operacao == '/':
    res_divisao = divisao(valor1, valor2)
    print(f'{res_divisao}')

elif operacao == '*':
    res_multiplica = multiplica(valor1, valor2)
    print(f'{res_multiplica:.0f}')
