numero = int (input("Digite um número"))
divisores = 0
contador = 1
while contador <= numero:
    if numero % contador == 0:
        divisores += 1
    contador += 1

if divisores == 2:
    print("O número é primo")
else:
     print("O número não é primo")   
