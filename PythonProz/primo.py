numero = int (input("Digite um número"))
if numero <= 1:
    print ("Esse número não é primo")
else:
    if numero % 2 != 0 and numero % 3 != 0 and numero % 7 != 0 and numero % numero == 0:
        print (" O número", numero , "é primo")
    else:
        print (" O número", numero, " não é primo")    