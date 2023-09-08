num = int (input('Digite um número'))
for a in range (1,num + 1):
    if num % a == 0:
        print('\033[33m',end=' ')
    else:
        print('\033[31m',end=' ')
    print('{} '.format(a), end=' ')