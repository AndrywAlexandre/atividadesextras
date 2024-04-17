n1=float(input('Digite o primeiro VALOR: '))
n2=float(input('Digite o segundo VALOR: '))
if n1 > n2:
    print('O primeiro valor {} é o maior'.format(n1))
elif n1 < n2:
    print('O segundo valor {} é o maior'.format(n2))
else:
    print('Os dois valores {} e {} são iguais'.format(n1,n2))