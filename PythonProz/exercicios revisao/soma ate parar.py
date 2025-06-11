#Soma até parar:
#Peça números ao usuário até ele digitar 0.
#Some todos os números digitados e mostre o resultado no final.

numero = 1
soma = 0

while numero != 0:
    numero = int(input ("Digite um numero. Para parar digite 0"))
    soma += numero 
print ("A soma dos números digitados foi: ", soma)    