#Construa um programa que ordene os elementos de um vetor em ordem crescente.

vet = []

quantidade = int (input ("Quantos números você deseja digitar?"))

contador = 0

while contador < quantidade:
    num = int (input("Digite um número:"))
    vet.append (num)
    contador += 1
print ("Vetor digitado: ", vet)

for i in range (quantidade -1):
    for j in range (quantidade -1):
        if vet [i] > vet [j]:
            vet [i], vet [i + 1] = vet [i + 1], vet [i]
print ("Vetor em ordem crescente: ", vet)                       