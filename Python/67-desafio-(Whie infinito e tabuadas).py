'''
num=0
conti=str=S

while True:
    num=int(input('Qual a Tabuada que Você gostaria de Analisar:'))
    print(f
        {num} x 1 = {num*1}
        {num} x 2 = {num*2}
        {num} x 3 = {num*3}
        {num} x 4 = {num*4}
        {num} x 5 = {num*5}
        {num} x 6 = {num*6}
        {num} x 7 = {num*7}
        {num} x 8 = {num*8}
        {num} x 9 = {num*9}
        {num} x 10= {num*10}
    )
    conti=str(input('Quer Continuar?'))
    if conti !=S:
        break 
erro Corrigir
'''
while True:
    num=int(input('digira um número'))
    if num<0:
        break
    for c in range (1,11):
        print(f'{num} x {c} = {num*c}')
print("acabou")
