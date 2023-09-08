while True:

    sexo=' '
    while sexo not in 'MmFf':
        sexo=str(input('Digite o Sexo da pessoa [M/F]:')).strip().upper()[0]
    idade=int(input('digite a idade'))
    total18=0
    homen=0
    mulher20=0
    if idade > 18:
        total18+=1
    if sexo=='M':
        homen+=1
    if sexo=='F' and idade<20:
        mulher20+=1
    resp = ' '
    while resp not in 'NnSs':
        resp = str(input('quer continuar [S/N]')).strip().upper()[0]
    if resp == 'N':
            break
print('obrigador por participar')
print(f'Pessoas maiores de 18 anos {total18}')
print(f'Homens cadastrados {homen}')
print(f'Mulheres menores de 20{mulher20}')