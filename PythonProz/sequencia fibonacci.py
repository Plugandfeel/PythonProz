#Peça ao usuário para digitar um numero
#mostrar a sequencia fibonacci até o numero que o usuario digitou
numero = int (input("Digite um numero"))

primeiro = 0
segundo= 1

i = 3
print (primeiro, segundo,)
while i <= numero:
    atual = primeiro + segundo
    print (primeiro, segundo, atual)
    primeiro = segundo
    segundo = atual
    atual = primeiro + segundo
    i = i + 1
    

   