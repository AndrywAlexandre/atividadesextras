import random
n1= str (input('primeiro nome da lista'))
n2= str (input('segundo nome da lista'))
n3= str (input('terceiro nome da lista'))
n4= str (input('quarto nome da lista'))
lista = [n1,n2,n3,n4]
#escolhe uma da lista
escolhido = random.choice(lista)
print('o nome escolido é {} '.format(escolhido))