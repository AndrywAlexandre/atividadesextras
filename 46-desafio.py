from time import sleep
n = input('Qual o seu Nome:')
print('Esse {} programa tem como finalidade uma contagem regreciva para os fogos de artificio'.format(n))
sleep(5)
for contador in range(10,-1,-1):
    print(contador)
    sleep(0.5)
print('BOOOOM POOOOW')