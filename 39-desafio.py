from datetime import date
dta = date.today().year
dtn = int(input('Qual a data do seu nascimento?'))
dtal = dtn + 18
if dtal == dta:
    print('O seu alistamento é esse ano')
elif dtal < dta:
    print ('seu alistamento já passou, o ano de alistamento foi {}'.format(dtal))
else:
    print('o seu ano de alistamento é em {}'.format(dtal))
