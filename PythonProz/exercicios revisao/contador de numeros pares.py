#Contador de números pares:
#Peça 5 números ao usuário e salve em uma lista.
#Mostre apenas os que são pares.

numeros = []
numerosPares = []
contador = 0

while contador < 5:
    numero = int(input ("Digite um numero"))
    numeros.append (numero)
    contador += 1
print ("Numeros digitados: ", numeros)   

for i in range (0, 5):
    if numeros [i] % 2 == 0:
        numerosPares.append (numeros [i])

print ("Números pares digitados: ", numerosPares)        
