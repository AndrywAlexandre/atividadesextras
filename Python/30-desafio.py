n = int(input('Digite um número para descobrir se ele é par ou impar: '))
r = n % 2
if r == 0:
    print('esse número {} é par!!'.format(n))
else:
    print('esse número {} é impar!!'.format(n))