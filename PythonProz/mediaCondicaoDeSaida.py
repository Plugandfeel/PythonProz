nota = float(input ("Digite uma nota"))
soma = 0
numero = 0

while nota >= 0:
    soma += nota
    numero += 1
    media = soma / numero
    nota = float (input ("Digite uma nota"))
print ( "A media das notas digitas foi", media)   
