#Criar um programa que verifique se um numero é primo e em seguida
#adicione esse numero a um vetor de numeros primos

num = 0
vetp = []
vetb = []

quantidade = int(input("Quantos números você deseja digitar?"))

contador = 0
while contador < quantidade:
    num = int(input("Digite um número para a ordem dos primos:"))
    count = 1
    divisor = 0

    while count <= num:
        if num % count == 0:
            divisor += 1
        count += 1
    if divisor == 2:
        #print (f' O numero {num}  é primo')
        vetp.append (num)
    else:
        #print (f' O número {num} não é primo')
        vetb.append (num)
    contador += 1
print (f' SEus numeros primos são {vetp}\n Esses outros números não são primos; {vetb}')                    