#Escreva um programa que encontre e exiba o maior elemento em um vetor

vet = []
contador = 0
maior = 0
quantidade = 0
num = 0

quantidade = int (input ("Quantos números você vai digitar?"))

while contador < quantidade:
    num = int (input ("Digite um número"))
    vet.append (num)
    contador += 1

contador = 0
maior = vet[0]
posicao = 0

for i in range (1, quantidade):
    if vet [i] > maior:
        maior = vet [i]
        posicao = i
    contador += 1

print ("Vetor digitado: ", vet)
print ("Maior elemento: ", maior)
print ("Posição do maior elemento: ", posicao)