valor =  float (input ("Digite o valor do produto"))
desconto = float (input ("Digite o percentual de desconto"))
valorDesconto = 0
if valor >= 100:
    valorDesconto = valor * desconto/100
    valorPagar = valor - valorDesconto
    print ("O valor a pagar será:", valorPagar)
else:
    print ("Desconto aplicável para valores acima de 100")    



