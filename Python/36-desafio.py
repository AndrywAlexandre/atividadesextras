vc=float (input('Qual o valor do imovel a ser comprado?: '))
vs=float (input('Qual o valor do seu salário?: '))
t=int (input('Em quantos anos sera pago o imovel'))
tm = t*12
vp= vc/tm
ps = vs * (30/100)
if vp > ps:
    print('Não é possivel realizar o inprestimo pois o valor da parcela supera 30% do seu salario')
elif vp < ps:
    print('O seu emprestimo foi aprovado')
else:
    print('erro de processamento')