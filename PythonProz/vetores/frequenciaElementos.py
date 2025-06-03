#Peça aos alunos para criar um programa que conte quantas vezes um elemento aparece em um vetor.

vet = []
vet2 = []
quantidade = 0
num = 0
contador = 0
repeticoes = 0

quantidade = int (input ("Quantos números deseja digitar?"))

while contador < quantidade:
    num = int(input ("Digite um número"))
    vet.append (num)
    contador += 1
print ("Vetor Digitado: ", vet) 


for i in range (quantidade):
    repeticoes = 0
    for j in range (quantidade):
        if vet [i] == vet [j]:
            repeticoes += 1
            if repeticoes > 1 and vet [i] not in vet2:
                vet2.append (vet [i])
                
print ("Números digitados mais de uma vez: ", vet2)


