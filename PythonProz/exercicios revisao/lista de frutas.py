#Alterando a lista:
#Crie uma lista com 3 frutas.
#Troque a segunda fruta por outra.
#Mostre a lista atualizada.

frutas = []
numero = 3
contador = 0

while contador < 3:
    fruta = input ("Digite uma fruta")
    frutas.append (fruta)
    contador += 1
print ("Frutas digitadas: ", frutas)

frutas [1] = input ("Digite uma nova fruta")

print ("Lista de frutas modificada: ", frutas)
