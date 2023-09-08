
print('estamos em uma via pública a caminho do interior de repente aparece um radar!! com limite de velocidade de 80 km')
v=float(input('Qual a sua velocidade no momento em que passou pelo radar??:'))
if v < 80 :
    print('você passou dentro do limite de velocidade, parabéns')
else:
    multa = (v-80)*7
    print('você utrapassou o limite de velocidade você deve pagar uma multa de R${:.2f}'.format(multa))
