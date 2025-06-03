vet = []
contador = 0
numero_escolhido = 0
repeticoes = 0

quantidade = int(input ("Quantos números você deseja digitar no vetor?"))

while contador < quantidade:
    num = int (input (" Digite um número para o vetor:"))
    vet.append (num)
    contador += 1

numero_escolhido = (int (input ("Qual número você deseja saber se repetiu?")))

if numero_escolhido in vet:
    for i in range (quantidade):
        if vet [i] == numero_escolhido:
            repeticoes += 1

else:
    print (f'número escolhido não está no vetor! O vetor digitado foi {vet}')   

print (f'Vetor digitado {vet}, o número escolhido foi {numero_escolhido}, ele repete {repeticoes} vezes.')             

