somaidade = 0
mediaidade = 0
for r in range (1 ,5):
    print('------{}ºPessoa------'.format(r))
    nome = str(input('Nome completo')).strip()
    idade= int(input('idade'))
    sexo = str(input('Sexo {M/F}')).strip()
    somaidade = somaidade + idade
print(somaidade)