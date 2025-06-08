
def verifica_primo (numero):
    divisor = 0
    contador = 1
    
    while contador <= numero:
        if numero % contador == 0:
            divisor += 1    
        contador += 1
    return divisor

def testeDivisores (divisoresFinal):

        if divisoresFinal == 2:
            print (f'O número {numero} é primo.')
        else:
            print (f'O número {numero} não é primo.')              

   
    
numero = int(input ("Digite um número para saber se ele é primo"))
divisoresFinal = verifica_primo (numero)
testeDivisores(divisoresFinal)




