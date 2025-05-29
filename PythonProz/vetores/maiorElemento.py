#Escreva um programa que encontre e exiba o maior elemento em um vetor.

vet = []
maior = 0
contador = 0

while contador < 5:
    num = int (input ("Digite um valor para o vetor"))
    vet.append (num)
    if vet [contador] > maior:
        maior = vet [contador]
    contador = contador + 1            
print ("Vetor: ", vet)
print ("Maior elemento do vetor: ", maior)        
