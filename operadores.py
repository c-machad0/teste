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
