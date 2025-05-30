#Peça aos alunos para criar um programa que conte quantas vezes um elemento aparece em um vetor.

vet = []
vet2 = []
contador = 0

quantidade = int (input ("Quantos números você deseja digitar?"))



while contador < quantidade:
    numero = int (input ("Digite um número"))
    vet.append (numero)
    contador += 1
print ("Os números digitados foram: ", vet) 

for i in range (quantidade):
    for j in range ( i + 1, quantidade):
        if vet [i] == vet [j] and vet [i] not in vet2:  # Se o número se repetir e ainda não foi adicionado em vet2
            vet2.append (vet [i])
print (" Os números que foram digitados mais de uma vez foram: ", vet2)               
