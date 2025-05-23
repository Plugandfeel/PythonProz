import random

charmander = 1
squirtle = 2
bulbasaur = 3



vidaInimigo = 0
ataqueInimigo = 0
defesaInimigo = 0

vidaJogador = 0
ataqueJogador= 0
defesaJogador = 0



lista = [1,2,3]


print ("__" *35)
print()

print ("Bem Vindo! Qual Pokemon você quer Escolher?")
print()

print (" 1 - Charmander")
print (" 2 - Squirtle")
print (" 3- Bulbasaur")
print ()

print ("__" *35)
print ()



pokemon = int (input ("Digite o número do Pokemon correspondente"))

if pokemon == 1:
    print()
    print ("Você escolheu Charmander")

    vidaJogador = 100
    ataqueJogador = 30
    defesaJogador = 10
    vidaInimigo = 100
    ataqueInimigo = 25
    defesaInimigo = 15
    print (" Vida do Charmander : ", vidaJogador, " | " " Vida do oponente: ", vidaInimigo)

    print()


elif pokemon == 2:
    print()
    print ("Você escolheu Squirtle")
    vidaJogador = 100
    ataqueJogador = 30
    defesaJogador = 10
    vidaInimigo = 100
    ataqueInimigo = 25
    defesaInimigo = 15
    print (" Vida do Squirtle : ", vidaJogador, " | " " Vida do oponente: ", vidaInimigo)
    print()
else:
    print()
    print ("Você escolheu Bulbasaur") 
    vidaJogador = 100
    ataqueJogador = 30
    defesaJogador = 10
    vidaInimigo = 100
    ataqueInimigo = 25
    defesaInimigo = 15
    print (" Vida do Bulbasaur : ", vidaJogador, " | " " Vida do oponente: ", vidaInimigo)
    print() 

oponente = random.choice(lista)
if oponente == 1:
    print ("Seu oponente será o Charmander")
elif oponente == 2:
    print ("Seu oponente será o Squirtle")
else:
    print ("Seu oponente será o Bulbasaur")  

print ("__" *35)
print ()
print ("A BATALHA VAI COMEÇAR !")
print ()
print ("__" *35)
listaOponente = [1,2]
# escolher ação
while vidaJogador > 0 and vidaInimigo > 0:
    escolha = int (input (" O que você deseja fazer? 1 - atacar, 2 - defender, 3 - fugir"))
    acaoOponente = random.choice(listaOponente)
    
    if escolha == 1 and acaoOponente == 1:
        print ("Você escolheu atacar")
        print ("O oponente vai atacar")
        vidaJogador = vidaJogador - ataqueInimigo
        vidaInimigo = vidaInimigo - ataqueInimigo
        print  (" vida jogador: ", vidaJogador, "|", "Vida oponente: ", vidaInimigo)
    elif escolha == 2 and acaoOponente == 1:
        print (" Você escolheu defender ")
        print ("O oponente vai atacar")
        vidaJogador = vidaJogador - ataqueInimigo
        print  (" vida jogador: ", vidaJogador, "|", "Vida oponente: ", vidaInimigo)
    elif escolha == 1 and acaoOponente == 2:
        print ("Você escolheu atacar")
        print ("O oponente vai defender")
        vidaInimigo = vidaInimigo - ataqueJogador   
        print  (" vida jogador: ", vidaJogador, "|", "Vida oponente: ", vidaInimigo) 
    elif escolha == 2 and acaoOponente == 2:
        print (" Você escolheu defender ")
        print ("O oponente vai defender")
        vidaJogador = vidaJogador
        vidaInimigo = vidaInimigo
        print  (" vida jogador: ", vidaJogador, "|", "Vida oponente: ", vidaInimigo)
    elif escolha == 3:
        print (" Você escolheu fugir")
        print ("A batalha acabou")    
    
    else:
        print ("Digite um número válido: 1 - atacar, 2 - defender, 3 - fugir ")
        escolha = int (input (" O que você deseja fazer? 1 - atacar, 2 - defender, 3 - fugir"))
if vidaJogador > vidaInimigo:
    print ("Você ganhou") 
else:
    print ("Você perdeu")           