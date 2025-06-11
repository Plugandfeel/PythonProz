#Lista de compras:
#Crie uma lista com 5 itens que a pessoa digitar.
#Mostre essa lista na tela.

lista = []
contador = 0
while contador <5:
    item = input ("Digite um item para a lista")
    lista.append(item)
    contador += 1
print (lista)    