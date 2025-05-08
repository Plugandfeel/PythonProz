meuNumero = 8
numero = int(input ("Adivinhe o número"))

while numero != meuNumero:
    
    if numero > meuNumero:
        print ("É um número menor")
        numero = int (input("Adivinhe o número"))
        
    elif numero < meuNumero:
        print ("É um número maior")
        numero = int (input("Adivinhe o número"))
        
    else:
        print ("Você acertou")
           
