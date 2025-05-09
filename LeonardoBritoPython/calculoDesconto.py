valor =  float (input ("Digite o valor do produto"))
desconto = float (input ("Digite o percentual de desconto"))
valordesconto = valor * desconto/100
valorPagar = valor - valordesconto

print ("O valor a pagar será:", valorPagar)