#Desenvolva um programa que calcule a média dos elementos de um vetor.

vet = []
soma = 0
media = 0
contador = 0

while contador < 5:
    num = int (input("Digite um numero para o vetor"))
    vet.append (num)
    soma = soma + vet [contador]
    contador += 1
media = soma /5
print (vet)
print ("Média do vetor: ", media)    