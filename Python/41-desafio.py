l1= float(input('qual o valor do primeiro lado'))
l2= float(input('qual o valor do segundo lado'))
l3= float(input('qual o valor do terceiro lado'))
if l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2:
    print('temos um triangulo')
else:
    print('não temos um triangulo')