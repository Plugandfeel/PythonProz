#Notas de alunos:
#Peça 3 notas, armazene em uma lista e
#mostre a média.

notas = []
contador = 0
while contador < 3:
    nota = float(input("Digite uma nota"))
    notas.append(nota)
    contador += 1
media = (notas[0] + notas [1] + notas [2]) /3 

print (notas)
print("Média das notas: ", media)