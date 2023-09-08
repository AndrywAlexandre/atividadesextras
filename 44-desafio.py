vlr = float(input('Qual o valor da Compra?:'))
print('''Escolha uma forma de pagamento:
[1] Pagamento a Vista
[2] Pagamento a Vista no Cartão
[3] Pagamento em até 2x no Cartão
[4] Pagamento 3x ou mais no cartão
''')
op = int(input('Qual a opção escolhida?:'))
if op == 1:
    av = vlr * 0.90
    print(av)
elif op == 2:
    ac = vlr * 0.95
    print(ac)
elif op == 3:
    p = int(input('Quantas parcelas ira dividir'))
    if 0 < p <= 2:
        c = vlr / p
        print (c)
    else:
        print('para dividir em mais parcelas selecione a opção 4 e para pagamentos a vista selecione as opções 1 ou 2')
elif op == 4:
    a3p=int(input('Quantas parcelas ira dividir'))
    vr = vlr * 1.20
    vf = vr / a3p
    print('o valor reajudatado foi {} e o valor das parcelas foi {} e a qunatidade de parcela foi {}'.format(vr,vf,a3p))
else:
    print('erro de informação')