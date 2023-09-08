import math
num= float(input('digita em número trigonometrico: '))
#pq eu tenho que colocar um conversor radians para ele retornar em radiano o sin?
seno=math.sin(math.radians(num))
#seno=math.degrees(math.sin(num))
print('o seno do ângulo {} é {:.2f}'.format(num,seno))
cosseno=math.cos(math.radians(num))
print('o cosseno do ângulo {} é {:.2f}'.format(num,cosseno))
tangente=math.tan(math.radians(num))
print('a tangente do ângulo {} é {:.2f}'.format(num,tangente))