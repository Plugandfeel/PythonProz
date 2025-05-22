import random

charmander = 1
squirtle = 2
bulbasaur = 3

vidaCharmander = 100
vidaSquirtler = 100
vidaBulbasaur = 100

ataqueCharmander = 30
ataqueSquirtler = 25
ataqueBulbasaur = 20

defesaCharmander = 10
defesaSquirtler = 15
defesaBulbasaur = 20

vidaInimigo = 100
#ataqueInimigo = 35
#defesaInimigo = 15



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
    print()
elif pokemon == 2:
    print()
    print ("Você escolheu Squirtle")
    print()
else:
    print()
    print ("Você escolheu Bulbasaur") 
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

escolha = int (input (" O que você deseja fazer? 1 - atacar, 2 - defender, 3 - fugir"))

while vidaCharmander or vidaBulbasaur or vidaSquirtler  > 0:
    if escolha == 1:
        print ("Você escolheu atacar")
    elif escolha == 2:
        print (" Você escolheu defender ")
    elif escolha == 3:
        print (" Você escolheu fugir")
        print ("A batalha acabou")
    else:
        print ("Digite um número válido: 1 - atacar, 2 - defender, 3 - fugir ")

    

# Opção ataque pokemon charmander contra todos os oponentes 

if escolha == 1 and pokemon == 1 and oponente == 1:
        if ataqueCharmander > defesaCharmander:
            resultado = ataqueCharmander - defesaCharmander
            vidaInimigo = vidaInimigo - (ataqueCharmander - defesaCharmander)    
        print ("Você causou ", resultado, " de dano")
        print ("Vida Charmander - ", vidaCharmander, "Vida do Oponente - ", vidaInimigo)
elif escolha == 1 and pokemon == 1 and oponente == 2:
        resultado = ataqueCharmander - defesaSquirtler
        vidaInimigo = vidaInimigo - (ataqueCharmander - defesaSquirtler)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Charmander - ", vidaCharmander, "Vida do Oponente - ", vidaInimigo)
elif escolha == 1 and pokemon == 1 and oponente == 3:
        resultado = ataqueCharmander - defesaBulbasaur
        vidaInimigo = vidaInimigo - (ataqueCharmander - defesaBulbasaur)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Charmander - ", vidaCharmander, "Vida do Oponente - ", vidaInimigo) 
        #opção defesa charmander contra todos os oponentes    
elif escolha == 2 and pokemon == 1 and oponente == 1:
        resultado = ataqueCharmander - defesaCharmander
        vidaCharmander = vidaCharmander - resultado
        print ("Você recebeu", resultado, " de dano")
        print ("Vida Charmander - ", vidaCharmander, "Vida do Oponente - ", vidaInimigo)
elif escolha == 2 and pokemon == 1 and oponente == 2:
        resultado = ataqueSquirtler - defesaCharmander 
        vidaCharmander = vidaCharmander - resultado
        print ("Você recebeu ", resultado, " de dano")
        print ("Vida Charmander - ", vidaCharmander, "Vida do Oponente - ", vidaInimigo)
elif escolha == 2 and pokemon == 1 and oponente == 3:    
        resultado = ataqueBulbasaur - defesaCharmander 
        vidaCharmander = vidaCharmander - resultado
        print ("Você recebeu ", resultado, " de dano") 
        print ("Vida Charmander - ", vidaCharmander, "Vida do Oponente - ", vidaInimigo) 
        #opção ataque squirtle contra todos
elif escolha == 1 and pokemon == 2 and oponente == 1:
        resultado = ataqueSquirtler - defesaCharmander
        vidaInimigo = vidaInimigo - (ataqueSquirtler - defesaCharmander)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Squirtle - ", vidaSquirtler, "Vida do Oponente - ", vidaInimigo)
elif escolha == 1 and pokemon == 2 and oponente == 2:
        resultado = ataqueSquirtler - defesaSquirtler
        vidaInimigo = vidaInimigo - (ataqueSquirtler - defesaSquirtler)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Squirtle - ", vidaSquirtler, "Vida do Oponente - ", vidaInimigo)
elif escolha == 1 and pokemon == 2 and oponente == 3:
        resultado = ataqueSquirtler - defesaBulbasaur
        vidaInimigo = vidaInimigo - (ataqueSquirtler - defesaBulbasaur)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Squirtle - ", vidaSquirtler, "Vida do Oponente - ", vidaInimigo) 
        #opçao defesa squirtle contra todos
elif escolha == 2 and pokemon == 2 and oponente == 1:
        resultado = ataqueCharmander - defesaSquirtler
        vidaSquirtler = vidaSquirtler - resultado
        print ("Você recebeu", resultado, " de dano")
        print ("Vida Squirtle - ", vidaSquirtler, "Vida do Oponente - ", vidaInimigo)
elif escolha == 2 and pokemon == 2 and oponente == 2:
        resultado = ataqueSquirtler - defesaSquirtler
        vidaSquirtler = vidaSquirtler - resultado
        print ("Você recebeu ", resultado, " de dano")
        print ("Vida Squirtle - ", vidaSquirtler, "Vida do Oponente - ", vidaInimigo)
elif escolha == 2 and pokemon == 2 and oponente == 3:    
        resultado = ataqueBulbasaur - defesaSquirtler
        vidaSquirtler = vidaSquirtler - resultado
        print ("Você recebeu ", resultado, " de dano") 
        print ("Vida Squirtle - ", vidaSquirtler, "Vida do Oponente - ", vidaInimigo)
        #opção ataque bulbasaur contra todos
elif escolha == 1 and pokemon == 3 and oponente == 1:
        resultado = ataqueBulbasaur - defesaCharmander
        vidaInimigo = vidaInimigo - (ataqueBulbasaur - defesaCharmander)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Bulbasaur - ", vidaBulbasaur, "Vida do Oponente - ", vidaInimigo)
elif escolha == 1 and pokemon == 3 and oponente == 2:
        resultado = ataqueBulbasaur - defesaSquirtler
        vidaInimigo = vidaInimigo - (ataqueBulbasaur - defesaSquirtler)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Bulbasaur - ", vidaBulbasaur, "Vida do Oponente - ", vidaInimigo)
elif escolha == 1 and pokemon == 3 and oponente == 3:
        resultado = ataqueBulbasaur - defesaBulbasaur
        vidaInimigo = vidaInimigo - (ataqueBulbasaur - defesaBulbasaur)
        print ("Você causou ", resultado, " de dano")
        print ("Vida Bulbasaur - ", vidaBulbasaur, "Vida do Oponente - ", vidaInimigo) 
        #opção defesa bulbasaur contra todos
elif escolha == 2 and pokemon == 3 and oponente == 1:
        resultado = ataqueCharmander - defesaBulbasaur
        vidaBulbasaur = vidaBulbasaur - resultado
        print ("Você recebeu", resultado, " de dano")
        print ("Vida Bulbasaur - ", vidaBulbasaur, "Vida do Oponente - ", vidaInimigo)
elif escolha == 2 and pokemon == 3 and oponente == 2:
        resultado = ataqueSquirtler - defesaBulbasaur
        vidaBulbasaur = vidaBulbasaur - resultado
        print ("Você recebeu ", resultado, " de dano")
        print ("Vida Bulbasaur - ", vidaBulbasaur, "Vida do Oponente - ", vidaInimigo)
elif escolha == 2 and pokemon == 3 and oponente == 3:    
        resultado = ataqueBulbasaur - defesaBulbasaur
        vidaBulbasaur = vidaBulbasaur - resultado
        print ("Você recebeu ", resultado, " de dano") 
        print ("Vida Bulbasaur - ", vidaBulbasaur, "Vida do Oponente - ", vidaInimigo)         
        
        
