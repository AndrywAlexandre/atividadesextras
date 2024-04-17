from random import randint
import time
while True:
    player=int(input('Digite um número:'))
    comp=randint(0,11)
    soma=player+comp
    v=0
    tipo=' '
    while tipo not in 'PpIi':
        print('-'*30)
        tipo=str(input('Par ou Impar?[P/I]')).strip().upper()[0]
    if tipo=='P':
        if soma % 2 == 0:
            time.sleep(2)
            print('-' * 30)
            print('vc venceu')
            print(f'Você jogou {player} e o computador jogou {comp}')
            v+=1
        else:
            time.sleep(2)
            print('-' * 30)
            print(f'vc predeu e tem um total de vitorias{v}')
            print(f'Você jogou {player} e o computador jogou {comp}')
            break
            break
    if tipo=='I':
        if soma % 2 != 0:
            time.sleep(2)
            print('-' * 30)
            print('vc venceu')
            print(f'Você jogou {player} e o computador jogou {comp}')
            v+=1
        else:
            time.sleep(2)
            print('-' * 30)
            print(f'vc perdeu e tem um total de vitoria {v}')
            print(f'Você jogou {player} e o computador jogou {comp}')
            break
            break
print('Obrigado por participar!!')
