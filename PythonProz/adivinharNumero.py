meuNumero = 8
numero = 0

while numero != meuNumero:
    numero = int (input("Adivinhe o número"))

    if numero > meuNumero:
        print ("É um número menor")
        
    elif numero < meuNumero:
        print ("É um número maior")
        
    else:
        print ("Você acertou")
           
