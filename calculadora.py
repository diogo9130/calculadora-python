# Mini calculadora

numero1 = float(input('Escolha o primeiro número: '))
numero2 = float(input('Escolha o segundo número: '))
operador = input('Escolha o operador desejado:')

if operador == '+':
    print('O operador escolhido foi +')
    print(f'O resultado é: {numero1 + numero2}')
    
elif operador == '-':
    print('O operador escolhido foi -')
    print(f'O resultado é: {numero1 - numero2}')
    



