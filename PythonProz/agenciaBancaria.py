print ("=="*20)
print ()
print ("Bem-Vindo ao Banco BLM !")
print ("Aqui seu dinheiro tem valor!")
print ()
print ("=="*20)

print ("Primeiro Digite o que você deseja fazer hoje")
print ("Digite 1 - para acessar sua conta")
print ("Digite 2 - para criar uma conta")
acao = int(input("O que você deseja fazer?"))
nome = ""

if acao == 1:
    print ("Muito Bem. Digite abaixo seu CPF e sua senha")
    cpf = int (input ("Digite seu cpf"))
    senha = int (input ("Digite seu sua senha"))
    
    

elif acao == 2:
    print ("Será um prazer ter você junto conosco! Vamos começar seu cadastro")
    nome = input ("Digite seu nome completo")
    cpf = int(input("Digite seu CPF"))
    senha = int (input ("Digite uma senha de 6 dígitos"))
    confereSenha = int (input ("Digite novamente sua senha"))
    if senha != confereSenha:
        print ("As senhas não conferem! Vamos tentar de novo?") 
        senha = int (input ("Digite uma senha de 6 dígitos"))
        confereSenha = int (input ("Digite novamente sua senha"))         
        
        print ("=="*20)
        print ()
        print ("Dados Cadastrados:")
        print ("Nome:", nome)
        print ("CPF:", cpf)
        print ("Senha: ******")
        print()
        print ("=="*20)
        print()
print ("=="*20)
print()
print ("     MENU")
saldo = 500
saque = 0
deposito = 0
transferencia = 0
print(" 1 - Saldo")
print (" 2 - Saque")
print (" 3 - Depósito")
print (" 4 - Tranferência")
print (" 5 - Extrato")
print (" 6 - Sair")
print ()
print ("=="*20)

menu = int (input ("Digite a opção desejada"))
while menu < 1 or menu > 6:
    print ("Digite um numero válido. ")
    print ("=="*20)
    print()
    print ("   MENU")
    
    print(" 1 - Saldo")
    print (" 2 - Saque")
    print (" 3 - Depósito")
    print (" 4 - Tranferência")
    print (" 5 - Extrato")
    print (" 6 - Sair")
    print()
    print ("=="*20)
    menu = int (input ("Digite a opção desejada"))
    #opções do menu
if menu == 1:
    print ("Seu saldo é R$ ", saldo, " reais" )
elif menu == 2:
    if saldo > 0:
        
        saque = float (input("Digite o valor que deseja sacar"))
        saldo = saldo - saque
        print ("=="*20)
        print()
        print (" Saque no valor de R$ ", saque, " reais")
        print (" Saldo : R$ ", saldo, " reais")
    else:
        print (" Você não tem saldo suficiente para realizar um saque.")
elif menu == 3:
    deposito = float (input (" Digite o valor que deseja depositar"))  
    saldo += deposito
    print ("=="*20)
    print()
    print (" Depósito no valor de R$ ", deposito, " reais")
    print (" Saldo : R$ ", saldo, " reais")
    print()
    print ("=="*20)
elif menu == 4:
    if saldo > 0:
        transferencia = float (input (" Digite o valor que você deseja transferir"))
        cpf2=int(input("Digite o cpf de quem vai receber a transferência"))
        if saldo >= transferencia:
            saldo -= transferencia
            print ("=="*20)
            print()
            print (" Transferencia no valor de R$ ", transferencia, " reais para o cpf ", cpf2)
            print (" Saldo : R$ ", saldo, " reais")
            print()
            print ("=="*20)
        else:
            print(" Saldo insuficiente para realizar transferencia") 
elif menu == 5:
    print ("=="*20)
    print()
    print ("           EXTRATO")
    print (" Saque no valor de R$ ", saque, " reais")
    print (" Depósito no valor de R$ ", deposito, " reais")
    print (" Transferencia no valor de R$ ", transferencia, " reais")
    print (" Saldo : R$ ", saldo, " reais")
    print ("=="*20)
    print()
else:
    print ("Obrigado! Volte sempre!")










