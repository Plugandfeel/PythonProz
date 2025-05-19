#Peça ao usuário para digitar um numero
#mostrar a sequencia fibonacci até o numero que o usuario digitou
numero = int (input("Digite um numero"))

primeiro = 1
segundo= 1
print (primeiro,segundo , end = " ")
i = 3
#print (primeiro, segundo, end = " & ")
while i <= numero:
    atual = primeiro + segundo
    primeiro = segundo
    segundo = atual
    i = i + 1
    print (atual, end =" ")    
    

   
