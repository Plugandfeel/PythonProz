#Peça o nome de uma pessoa 
# a quantidade de vezes que ela foi à academia essa semana.
# Mostre uma mensagem motivadora tipo: "Parabéns, João! Treinar 4 vezes na semana é top!"

nome = input("Qual o seu nome?")
quantidade = int (input ("Quantas vezes você foi à academia essa semana?"))

if quantidade < 3:
    print (" Poxa, ", nome, ",", quantidade, "vezes na semana é pouco!")
elif quantidade <=5:
    print (" Muito bom , ", nome, "!", quantidade, "com certeza o resultado vem!")
else:
    print (" Caramba, ", nome, "! ", quantidade, "vezes na semana! Você é uma máquina de treinar!")        