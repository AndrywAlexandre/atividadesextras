s = str(input('Digita o valor do sexo:')).strip().upper()[0]
while s not in 'MmFf':
    print('digite o valor M (caso seu sexo seja masculino) ou F(caso seu sexo seja feminino)')
    s=str(input('digite o valor novamente:')).strip().upper()[0]
print('informação Armazenada')
