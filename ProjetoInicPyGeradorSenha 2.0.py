import random

# maius=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',]
# Maiusculo 65 - 90 em ascii

# letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Minusculo 97 - 122 em ascii

# numer=['1','2','3','4','5','6','7','8','9','0',]

caracteres =['!','@','#','$','%','&','*','(',')','_','-','+','+','{','}','[',']','^','>','<',',','.','º','£','¬','|',]

def gerarMaiusculo(quantidade):
      senhaGerada = []
      for i in range(quantidade):
            senha = chr(random.randrange(65, 91))
            senhaGerada.append(senha)
      print(senhaGerada)
      #return "".join(elemento for elemento in senhaGerada)

def gerarMinusculo(quantidade):
  senhaGerada = []
  for i in range(quantidade):
        senha = chr(random.randrange(97, 123))
        senhaGerada.append(senha)

  return "".join(elemento for elemento in senhaGerada)

def gerarNumerico(quantidade):
  senhaGerada = []
  for i in range(quantidade):
        senha = random.randrange(0, 10)
        senhaGerada.append(senha)

  return "".join(str(elemento) for elemento in senhaGerada)

def gerarCarctereEspec(quantidade):
  senhaGerada = []
  for i in range(quantidade):
        aleatorio = random.randrange(0, len(caracteres))
        senha = caracteres[aleatorio]
        senhaGerada.append(senha)

  return "".join(elemento for elemento in senhaGerada)

def gerarMaiMIn(quantidade):
  senhaGerada = []
  for i in range(quantidade):
        aleatorio = random.randrange(1, 3)

        if aleatorio == 1:
            senha = gerarMaiusculo(1)
        elif aleatorio == 2:
            senha = gerarMinusculo(1)

        senhaGerada.append(senha)

  return "".join(elemento for elemento in senhaGerada)

def gerarMaiMinNum(quantidade):
  senhaGerada = []

  for i in range(quantidade):
        aleatorio = random.randrange(1, 4)

        if aleatorio == 1:
            senha = gerarMaiusculo(1)
        elif aleatorio ==2:
            senha = gerarMinusculo(1)
        elif aleatorio == 3:
            senha = gerarNumerico(1)

        senhaGerada.append(senha)

  return "".join(str(elemento) for elemento in senhaGerada)

def gerarMaiMInNumCarctEs(quantidade):
  senhaGerada = []

  for i in range(quantidade):
        aleatorio = random.randrange(1, 5)

        if aleatorio == 1:
            senha = gerarMaiusculo(1)
        elif aleatorio == 2:
            senha = gerarMinusculo(1)
        elif aleatorio == 3 :
            senha = gerarNumerico(1)
        elif aleatorio == 4:
            senha = gerarCarctereEspec(1)

        senhaGerada.append(senha)

  return "".join(str(elemento) for elemento in senhaGerada)

while True:
    #saber a quantidade de caracteres
    print('Gerador de Senha Automatica')
    print('''++++ OPÇÕES PARA ESTRUTURA DAS SENHAS ++++
    
    - Para gerar senha precisamos de algumas informações
    - Para gerar senhas somente com letras maiusculas digite [1]
    - Para gerar senhas somente com letras minusculas digite [2]
    - Para gerar senhas somente com números digite [3]
    - Para gerar senhas somente com caracteres especiais [4]
    - Para gerar senhas com letras maiusculas e minusculas digite [5]
    - Para gerar senhas com letras maiusculas ,minusculas e números [6]
    - Para gerar senhas com letras maiusculas ,minusculas, números e caracteres especiais[7]
    ''')

    opcao=int(input('Digite a opção escolhida: '))
    Quant=int(input('Digite a quantidade de Caracteres que deve conter na Senha: '))


    if opcao == 1:
        print(gerarMaiusculo(Quant))
    elif opcao == 2 :
        print(gerarMinusculo(Quant))
    elif opcao == 3:
        print(gerarNumerico(Quant))
    elif opcao == 4:
        print(gerarCarctereEspec(Quant))
    elif opcao == 5:
        print(gerarMaiMIn(Quant))
    elif opcao == 6:
        print(gerarMaiMinNum(Quant))
    elif opcao == 7:
        print(gerarMaiMInNumCarctEs(Quant))

    opcao = input("Para gerar uma nova senha [1]\nSair [2]")

    if opcao == 1:
        pass
    elif opcao == 2:
        break
Print('obrigado por participar')
