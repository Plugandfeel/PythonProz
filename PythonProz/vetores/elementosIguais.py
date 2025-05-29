#Peça aos alunos para criar um programa que conte quantas vezes um elemento aparece em um vetor.

vet = []
vet2 = []
contador = 0

while contador < 5:
    numero = int (input ("Digite um número"))
    vet.append (numero)
    contador += 1
print ("Os números digitados foram: ", vet) 

for i in range (4):
    for j in range (4):
        if vet [j] == vet [j + 1]:
            vet2.append (vet [j])
print (" Os números que foram digitados mais de uma vez foram: ", vet2)           