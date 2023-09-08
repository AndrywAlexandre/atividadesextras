soma=conta=menor=maiormil=0
while True:
    nomep=str(input('Digite o Nome do produto'))
    valorp=int(input('Digite o valor do Produto em R$'))
    conta+=1
    soma = soma + valorp
    novonome=' '
    if valorp > 1000:
        maiormil+=1
    if conta==1:
        menor=valorp
        novonome = nomep
    else:
        if menor > valorp:
            menor = valorp
            novonome = nomep
    cont=' '
    while cont not in 'SsNn':
        cont=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if cont == 'N':
        break
print(soma)
print(menor)
print(maiormil)
print(novonome)

''' aparentimente esta com erro depois de 3 coisas não apatece o nome
'''

