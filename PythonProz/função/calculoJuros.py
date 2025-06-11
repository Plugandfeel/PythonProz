def calcularMontante (principal, taxa, ano):
    montante = principal + (principal*taxa*ano/100)
    return montante




principal = float(input("Digite o valor principal: "))
taxa = float(input("Digite a Taxa: "))
ano = float(input("Digite o número de anos: "))
valorMontante = calcularMontante (principal, taxa, ano)

print("O valor total da taxa será de:", valorMontante)