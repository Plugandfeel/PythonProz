#Crie um programa que:
#Peça o valor de um produto 
# a porcentagem de desconto (ex: 10%)
# Calcule e mostre o valor com desconto

valor =  float (input("Qual o valor do produto?"))
desconto = float (input ("Qual a porcentagem de desconto?"))

valorAbatido = valor * desconto / 100

valorCompra = valor - valorAbatido

print ("Valor original: ", valor)
print ("Valor do desconto: ", valorAbatido)
print ("Você irá pagar: R$ ", valorCompra, "reais.")