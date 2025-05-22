import random
print ("Bem Vindo! Qual Pokemon você quer Escolher")

print (" 1 - Charmander")
print (" 2 - Squirtle")
print (" 3- Bulbasaur")

charmander = 1
squirtle = 2
bulbasaur = 3
vidaCharmander = 100
vidaSquirtler = 100
vidaBulbasaur = 100

ataqueCharmander = 30
ataqueSquirtler = 25
ataqueBulbasaur = 15

defesaCharmander = 10
defesaSquirtler = 20
defesaBulbasaur = 35


lista = [1,2,3]

pokemon = int (input ("Digite o número do Pokemon correspondente"))

if pokemon == 1:
    print ("Você escolheu Charmander")
elif pokemon == 2:
    print ("Você escolheu Squirtle")
else:
    print ("Você escolheu Bulbasaur")  

oponente = random.choice(lista)
if oponente == 1:
    print ("Seu oponente será o Charmander")
elif oponente == 2:
    print ("Seu oponente será o Squirtle")
else:
    print ("Seu oponente será o Bulbasaur")  


print ("A BATALHA VAI COMEÇAR")

escolha = int (input (" O que você deseja fazer? 1 - atacar, 2 - defender, 3 - fugir"))
if escolha == 1:
    print ("Você escolheu atacar")
elif escolha == 2:
    print (" Você escolheu defender ")
else:
    print (" Você escolheu fugir")
    print ("A batalha acabou")
  

if escolha == 1 and oponente == 1:
        resultado = ataqueCharmander - defesaCharmander
        print ("Você causou ", resultado, " de dano")
elif escolha == 1 and oponente == 2:
        resultado = ataqueCharmander - defesaSquirtler
        print ("Você causou ", resultado, " de dano")
elif escolha == 1 and oponente == 3:
        resultado = ataqueCharmander - defesaBulbasaur
        print ("Você causou ", resultado, " de dano")

if escolha == 2 and oponente == 1:
        resultado = ataqueCharmander - defesaCharmander
        vidaCharmander = vidaCharmander - resultado
        print ("Você recebeu", resultado, " de dano")
        print ("Você tem ", vidaCharmander, " de vida.")
elif escolha == 2 and oponente == 2:
        resultado = defesaCharmander - ataqueSquirtler
        vidaCharmander = vidaCharmander - resultado
        print ("Você recebeu ", resultado, " de dano")
        print ("Você tem ", vidaCharmander, " de vida.")
elif escolha == 2 and oponente == 3:    
        resultado = defesaCharmander - ataqueBulbasaur
        vidaCharmander = vidaCharmander - resultado
        print ("Você recebeu ", resultado, " de dano") 
        print ("Você tem ", vidaCharmander, " de vida.")   
   

      




