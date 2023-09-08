num: int=0
contaguem=0
soma=0
while True:
    num = int(input('digita o numero:'))
    print('-'*20)
    if num == 999:
        break
    soma += num
    contaguem += 1
print(f'o valor da soma{soma} e a quantidade de números é {contaguem}')