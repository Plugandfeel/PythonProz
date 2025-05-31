#Peça aos alunos para criar um programa que inverta a ordem dos elementos em um vetor.

vet = []
vetInvertido = []
quantidade = 0
num = 0
contador = 0

quantidade = int (input ("Quantos números você deseja digitar?"))

while contador < quantidade:
    num = int (input ("Digite um número:"))
    vet.append (num)
    contador += 1
print ("Vetor Digitado: ", vet)    

for i in range (quantidade -1, -1, -1):
    vetInvertido.append (vet [i])

print ("Vetor Invertido: ", vetInvertido)   


