print(f'{'CALCULADORA SIMPLES':=^40}')

num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))
adicao = num1 + num2
sub = num1 - num2
div = num1 / num2
multi = num1 * num2
print('[1] Adição')
print('[2] Subtração')
print('[3] Divisão')
print('[4] Multiplicação')
operacao = int(input('Escolha uma das opções: '))
print('-' * 40)

if operacao == 1:
    print(f'{num1} + {num2} = {adicao}')
elif operacao == 2:
    print(f'{num1} - {num2} = {sub}')
elif  operacao == 3:  
    print(f'{num1} / {num2} = {div}')
elif operacao == 4:
    print(f'{num1} * {num2} = {multi}')
else:
    print('Valor inválido, tente novamente.')
