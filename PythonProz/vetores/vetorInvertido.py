#Peça aos alunos para criar um programa que inverta a ordem dos elementos em um vetor

vet = []
for i in range (5):
    num = int (input ("Digite um numero para o vetor"))
    vet.append (num)
vet_invertido = []
# esse for começa em 4 vai até antes de -1, e diminui de 1 em 1
for i in range (4, -1, -1):
    vet_invertido.append (vet [i])


print("Vetor invertido:", vet_invertido)