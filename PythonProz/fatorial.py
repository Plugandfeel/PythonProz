numero = int (input ("Digite um numero"))
multiplicacao = 0
soma = 0
while numero > 1:
    for i in range (numero, 1):
        multiplicacao = i * numero
        soma += multiplicacao
    
print ("O fatorial de ", numero, " é: ", soma)
