def verificaTriangulo (lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        print ("Triangulo equilatero")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print ("Triangulo escaleno ")
    else:
        print ("Triangulo isosceles")


lado1 = float (input ("Digite o comprimento do primeiro lado do triangulo"))
lado2 = float (input ("Digite o comprimento do segundo  lado do triangulo"))
lado3= float (input ("Digite o comprimento do terceiro lado do triangulo"))

verificaTriangulo (lado1, lado2, lado3)