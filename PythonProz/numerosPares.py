num1 = int (input ("Digite um número"))
num2 = int (input ("Digite outro número"))
num3 = 0


if num1 > num2:
    
    num3 = num2
    num2 = num1
    for i in range (num3 + 1, num2):
        if i % 2 == 0:
            print (i)
else:
    for i in range (num1 + 1, num2):
        if i % 2 == 0:
            print (i)            


