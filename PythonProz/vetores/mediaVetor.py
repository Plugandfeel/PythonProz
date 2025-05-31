#Desenvolva um programa que calcule a média dos elementos de um vetor.

vet = []
soma = 0
media = 0
contador = 0
num = 0

quantidade = int (input ("Quantos numeros você vai digitar?"))

while contador < quantidade:
    num = float (input ("Digite um número para o vetor:"))
    vet.append (num)
    soma += num
    contador += 1

media = soma / quantidade

print ("Vetor digitado: ", vet)
print ("Média dos valores do vetor: ", media)
