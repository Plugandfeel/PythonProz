#Construa um programa que ordene os elementos de um vetor em ordem crescente

vet = []
for i in range (0,5):
    num = int (input ("Digite um numero para o vetor"))
    vet.append (num)
print (vet)

tamanho = 5

for i in range (4):
    for j in range (4):
        if vet [j] > vet [j + 1]:
            vet [j], vet [j + 1] = vet [j + 1], vet [j]
print (vet)            