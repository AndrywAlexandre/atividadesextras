from random import randint
comp = randint(0,10)
print('olá eu sou o seu computador qual numero eu estou pensando?')
vd=int(input('digite o número que pensei:'))
quant = 1
while vd != comp:
    if vd > comp:
        quant += 1
        vd = int(input('O valor que pensei foi menor, digite novamente:'))
    if vd < comp:
        quant += 1
        vd=int(input('O valor que pensei foi maior, digite novamente:'))
print('vc acertou !!! vc precisou de {} tentativas'.format(quant))

'''
Resposta Guanabara.
from random inport randint
computador =randint(1,10)
print('Sou seu comp... digite um número')
acertou=False
palpites=0
while not acertou:
    jogador=int(input('qual o valor '))
    palpites +=1
    if jogador == acertou:
        acertou = true
    else:
        if jogador < computador:
            print('mais... digite novamente')
        else jogador > computador :
            printe ('menor... digita novamente')
print('vc acertou com {} tentativas'.format(palpites))
'''