contaguem=0
num=0
soma=med=0
continua=0
maior=0
menor = num
while continua != "N":
    num=int(input('digite um número'))
    continua = str(input('Quer continuar (S/N) Só é aceito S ou N')).upper().strip()[0]
    contaguem += 1
    soma+=num
    med= soma/contaguem
    if contaguem == 1:
      maior=menor=num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor = num
print('A quantidade de Números foi {} o maior foi {} o menor foi {} e a media foi {}'.format(contaguem,maior,menor,med))
#print('Acabou !!')