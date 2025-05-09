lado1 = float (input ("Digite o comprimento do primeiro lado do triangulo"))
lado2 = float (input ("Digite o comprimento do segundo  lado do triangulo"))
lado3= float (input ("Digite o comprimento do terceiro lado do triangulo"))

if lado1 == lado2 and lado1 == lado3:
    print ("Triangulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print ("Triangulo isosceles ")
else:
    print ("Triangulo escaleno")    
