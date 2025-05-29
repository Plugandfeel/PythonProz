#Solicite aos alunos que criem um programa que verifique se um número é primo 
# e, em seguida, adicione esse número a um vetor de números primos.

# Inicializa o vetor para armazenar os números primos
numeros_primos = []

# Solicita ao usuário um número
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é primo (sem usar funções)
if numero > 1:
    eh_primo = True  # Assume que o número é primo inicialmente
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            eh_primo = False  # Se for divisível por algum número, não é primo
            break  # Não precisa continuar verificando
    
    # Se for primo, adiciona ao vetor
    if eh_primo:
        numeros_primos.append(numero)

# Imprime o vetor de números primos (se houver algum)
if numeros_primos:
    print("Números primos encontrados:", numeros_primos)
else:
    print("O número digitado não é primo.")    