from random import randint
from time import sleep
computado = randint(0,1)
print('=+='*20)
print('Tente adivinhar o númoro que eu pensei entre 0 e 3')
print('=+='*20)
n=int(input('o valor pensado pelo computador foi:'))
print('!!!PROCESSANDO!!!')
sleep(3)
if n==computado:
    print('Você acertou, !!!!parabéns!!!!')
else:
    print('Você errou o número que pensei foi {}'.format(computado))