print("Nosso Cardapio Temos: \n"
      "Refrigerante: 3,50 reais \n"
      "Bolo: 2,50 reais\n"
      "Água: 2,00 reais\n"
      "**Observação digite o nome do produto que você quer** \n")

Produto=str(input('Digite o nome do produto que você deseja: '))
Quantidade=int(input(f"\nDigite a quantidade de '{Produto}' você quer:"))
quero_mais=str(input("Deseja mais Alguma coisa? (USE Sim OU Não)"))

quero_mais=quero_mais.upper()
Produto=Produto.lower()


lista_compras={}
lista_compras [Produto]=Quantidade
while quero_mais == 'SIM':
    Produto=str(input('Digite o nome do produto que você deseja acresentar: '))
    Quantidade=int(input(f"\nDigite a quantidade de '{Produto}' você quer acresentar:"))
    if Produto in lista_compras:
        lista_compras[Produto].append(Quantidade)
    else: lista_compras[Produto]=Quantidade
    quero_mais = str(input("\nDeseja mais Alguma coisa? (USE SIM OU NÃO)"))
total_apagar=0
preço_unico=0
for Produto,Quantidade in lista_compras.items():
    if Produto == "refrigerante":
        preço_unico= 3.50
    if Produto == "bolo":
        preço_unico= 2.50
    if Produto == "água":
        preço_unico= 2.00

    total=preço_unico*Quantidade

    total_apagar=total_apagar + total

print(total_apagar)
