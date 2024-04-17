n=int(input('Digite um número inteiro: '))
print('''
[1] Para converter em binario 
[2] Para converter em octal
[3] Para converter em hexadecimal
''')
op=int(input('Sua opção é: '))
if op == 1:
    print('O valor convertido em binario é {}'.format(bin(n)[2:]))
elif op == 2:
    print('O valor convertido em binario é {}'.format(oct(n)[2:]))
elif op == 3:
    print('O valor convertido em binario é {}'.format(hex(n)[2:]))
elif op != 1 and op != 2 and op !=3:
    print('numeração invalida')