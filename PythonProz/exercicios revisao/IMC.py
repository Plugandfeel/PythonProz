#Peça a altura e o peso da pessoa 
# calcule o IMC:
# Fórmula: IMC = peso / (altura * altura)
# Mostre o resultado

altura = float (input("Digite sua altura"))
peso = float (input("Digite o seu peso"))

imc = peso / (altura * altura)

print ("Seu IMC é: ", imc)