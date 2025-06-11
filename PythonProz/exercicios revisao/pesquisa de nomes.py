#Pesquisa de nomes:
#Peça nomes até a pessoa digitar "sair".
# Mostre todos os nomes digitados e quantos foram.

nomes = []
nome = ""
quantidade = 0

while nome != "sair":
    nome = input("Digite um nome ou digite sair para sair")
    if nome == "sair":
        break
    else:
        nomes.append(nome)
        quantidade += 1
print("Total de nomes digitados: ", quantidade)
print ("nomes digitados: ", nomes)    