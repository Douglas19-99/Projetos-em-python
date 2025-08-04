print(f'{'CALCULADORA SIMPLES':=^40}')
while True: 
    try:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
        print('[1] Adição')
        print('[2] Subtração')
        print('[3] Divisão')
        print('[4] Multiplicação')
        print('[5] Sair')
        operacao = int(input('Escolha uma das opções: '))
        print('-' * 40)

        if operacao == 1:
            adicao = num1 + num2
            print(f'{num1} + {num2} = {adicao}')
        elif operacao == 2:
            sub = num1 - num2
            print(f'{num1} - {num2} = {sub}')
        elif  operacao == 3:
            if num2 == 0:
                 print('ERRO: Não é possível dividir por ZERO.')
            else:
                div = num1 / num2  
                print(f'{num1} / {num2} = {div}')
        elif operacao == 4:
            multi = num1 * num2
            print(f'{num1} * {num2} = {multi}')
        elif operacao == 5:
             print('Encerrando a calculadora. Até logo!')
             break
        else:
             print('Valor inválido. Por favor, Insira apenas números.')
    except ValueError:
            print('Valor inválido, tente novamente.')
    except Exception as e:
         print(f'Ocorreu um erro inesperado: {e}')
    