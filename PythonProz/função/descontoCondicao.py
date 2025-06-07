def calculo_desconto(valor):
    valorDesconto = 0 
    valorDesconto = valor * desconto/100
    valorPagar = valor - valorDesconto
    print ("O valor a pagar será:", valorPagar)


valor =  float (input ("Digite o valor do produto"))
desconto = float (input ("Digite o percentual de desconto"))

if valor >= 100:
    calculo_desconto (valor) 
else:
    print ("Desconto aplicado apenas para compras acima de 100 reais.")       



