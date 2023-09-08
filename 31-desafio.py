dis = float(input('Qual a distância que vc vai viajar em KM: '))
if dis <= 200:
    vp = (dis * 0.50)
    print('o valor da sua viajem é R$ {}'.format(vp))
else:
    vd = (dis * 0.45)
    print('o valor da sua viajem é R${}'.format(vd))