#Crie um programa que some dois vetores de mesmo tamanho #
#  exiba o resultado.

vet1 = []
vet2 = []
contador = 0
vetSoma = []

while contador < 5:
    num1 = (int(input ("Digite um número para o vetor 1")))
    vet1.append (num1)
    contador += 1

contador = 0
while contador < 5:
    num2 = (int(input ("Digite um número para o vetor 2")))
    vet2.append (num2)
    contador += 1


contador = 0
while contador < 5:
    for i in range (0, 5):
        soma = vet1 [i] + vet2 [i]
        vetSoma.append (soma)
        contador += 1

print ("Vetor 1: ", vet1)
print ("Vetor 2: ", vet2)
print ("Vetor Soma: ", vetSoma)
        