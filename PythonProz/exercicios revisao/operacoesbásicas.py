#Pergunte dois números
#Mostre a soma, subtração, multiplicação e divisão dos dois números

numero1 = int(input("Digite um número"))
numero2 = int(input("Digite outro número"))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
if numero2 != 0:
    divisao = numero1/numero2

print ("soma dos dois números: ", soma)
print ("subtracao dos dois números: ", subtracao)
print ("divisao dos dois números: ", divisao)
print ("multiplicacao dos dois números: ", multiplicacao)
