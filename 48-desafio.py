#informação de acumuladores
soma = 0
contador= 0
for c in range(1,500,2):
    if c % 3 == 0:
        soma = soma + c
        contador +=1        #+= é igual a = soma +c
print('a soma foi de {} e a quantidades de números foi{}'.format(soma,contador))
