import random
maius=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numer=['1','2','3','4','5','6','7','8','9','0']
caract=['!','@','#','$','%','&','*','(',')','_','-','+','+','{','}','[',']','^','>','<',',','.','º','£','¬','|']
a=0
SenhaCri=[]
b=1
#saber a quantidade de caraquiteres
print('Gerador de Senha Automatica')
print('''++++ OPÇÕES PARA ESTRUTURA DAS SENHAS ++++

-Para gerar senha precisamos de algumas informações
-Para gerar senhas somente com letras maiusculas digite [1]
-Para gerar senhas somente com números digite [2]
-Para gerar senhas somente com letras minusculas digite [3]
-Para gerar senhas somente com caracteres especiais [4]
-Para gerar senhas com letras maiusculas e minusculas digite [5]
-Para gerar senhas com letras maiusculas minusculas e números [6]
-Para gerar senhas com letras maiusculas minusculas, números e caracteres especiais[7]
''')
opção=int(input('Digite a opção escolhida: '))
Quant=int(input('Digite a quantidade de Caracteres que deve conter na Senha: '))

if opção == 1:
    #saber se pode usar levas maiusculas
    while a < Quant:
        senha=random.sample(maius,1)
        SenhaCri+=senha
        a = a + 1
    print(*SenhaCri, sep='')
if opção == 2:
    #Saber e pode usar arquivos de números
    while a < Quant:
        senha=random.sample(numer,1)
        SenhaCri+=senha
        a = a + 1
    print(*SenhaCri, sep='')
if opção == 3:
    # saber se pode usar levas maiusculas
    while a < Quant:
        senha = random.sample(letras, 1)
        SenhaCri += senha
        a = a + 1
    print(*SenhaCri, sep='')
if opção == 4:
    #saber se pode usar caracteres especiais
    while a < Quant:
        senha=random.sample(caract,1)
        SenhaCri+=senha
        a=a+1
    print(*SenhaCri, sep='')
if opção == 5:
    while a < Quant:
        senha=random.sample(maius+letras,1)
        SenhaCri += senha
        a=a+1
    print(*SenhaCri, sep='')
if opção == 6:
    while a<Quant:
        senha=random.sample(maius+letras+numer,1)
        SenhaCri += senha
        a=a+1
    print(*SenhaCri, sep='')
if opção == 7:
    # saber se pode usar levas maiusculas
    while a < Quant:
        senha = random.sample(maius+letras+numer+caract, 1)
        SenhaCri += senha
        a = a + 1
    print(*SenhaCri, sep='')
