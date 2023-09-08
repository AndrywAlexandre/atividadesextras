import time
print('Esse Programa tem como finalidade treinar menu')
print('Digite dois número para fazer alguns cálculos')
v1 = int(input('digita o primeiro número:'))
v2 = int(input('digita o segundo número:'))
a = 0
menu = 0
while menu !=5:
    while a !=2:
        print('''        [1]Soma
        [2]Mutiplicação
        [3]Maior
        [4]Novos números
        ''')
        menu=int(input('Qual opção:'))
        if menu == 1:
            print(v1+v2)
            a = int(input('Executar novamente? (1/sim e 2/não):'))
        if menu == 2:
            print(v1*v2)
            a = int(input('Executar novamente? (1/sim e 2/não):'))
        if menu == 3:
            if v1 > v2:
                print(v1)
                a = int(input('Executar novamente? (1/sim e 2/não):'))
            else:
                print(v2)
                a = int(input('Executar novamente? (1/sim e 2/não):'))
        if menu == 4:
            v1 = int(input('digita o primeiro número:'))
            v2 = int(input('digita o segundo número:'))
            print('valores armarenados')
    time.sleep(5)
    menu=int(input('sair totalmente do programa digite 5 se deseja continuar digita 1:'))
time.sleep(6)
print('Boa Noite')