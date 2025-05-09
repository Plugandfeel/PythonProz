numero = int (input ("Digite um numero"))
if numero == 0 or numero == 1:
    print ("Fatorial igual a 1.")    
multiplicacao = numero
soma = 0
while numero > 1:
    multiplicacao = multiplicacao * (numero-1)
    numero = numero - 1

    
print ("O fatorial de ", numero, " é: ", multiplicacao)
