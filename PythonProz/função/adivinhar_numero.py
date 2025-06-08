import random
def adivinhacao (numero_escolhido):
    lista = []
    numero = 200
    contador = 1
    
    while contador <= numero:
        lista.append (contador)
        contador += 1 

    sorteado = random.choice (lista)


    contador = 0
    while numero_escolhido != sorteado:

        if numero_escolhido < sorteado:
            print ("Número escolhido maior")
            numero_escolhido = int(input("Tente adivinhar o número escolhido"))
            
        elif numero_escolhido > sorteado:
            print ("Número escolhido menor")  
            numero_escolhido = int(input("Tente adivinhar o número escolhido"))
            
    

    else:
        print (f"Você acertou o número escolhido, que foi {sorteado} ")

            
    

numero_escolhido = int(input("Tente adivinhar o número escolhido"))

adivinhacao (numero_escolhido)

      