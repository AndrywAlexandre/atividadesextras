"""
Se Nos usarmos um
if vl = int
    N=vl
else:
    N = parou
E então faria a Tratativa da string
"""
num = soma = cont = 0
num = int(input('digite um número para somar e digire 999 para parar'))
while num != 999:
    #num = int(input('digite um número para somar e digire 999 para parar'))
    cont += 1
    soma += num
    num = int(input('digite um número para somar e digire 999 para parar'))
print('A soma foi {} e a qantidade de números digitados foi {}'.format(soma, cont))
