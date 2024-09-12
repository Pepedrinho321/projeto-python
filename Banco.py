saldo = 2000
saque = 0
deposito = 0
extrato = ("Extrato =")
print ("""

==========Banco=========

1 - Saque
2 - Depósito
3 - Extrato
0 - Sair""")

limite_saque = 0
contador = 0

while contador == 0:
    acao = int(input("Insira o número da ação desejada: "))
    if acao == 1:
        if limite_saque == 3:
            print ("Limite de saques diário atingido, não foi possível finalizar a solicitação")
        else:
            saque = int(input("Digite o valor do saque desejado: "))
            if saque > 500:
                print ("Limite valor para saque de até R$500,00")
            elif saque <= saldo:    
                saldo -= saque
                limite_saque += 1
                print (f"Saque efetuado com sucesso no valor de {saque}, seu novo saldo é: {saldo}.")
                extrato += (f" \nSaque realizado no valor de = R${saque:,.2f}")
            else:
                print ("Saldo insuficiente para realizar o saque")
    elif acao == 2:
        deposito = int(input("Digite o valor desejado para depósito: "))
        if deposito < 1:
            print ("Depósito no valor de zero ou negativo não é permitido")
        else:
            saldo += deposito
            extrato += (f"\nDepósito realizado no valor de = {deposito}")
            print (f"Depósito realizado com sucesso, seu novo saldo é: {saldo}")
    elif acao == 3:
        print (extrato)
    elif acao == 0:
        print ("Obrigado por utilizar o banco XXXX")
        contador = 1
    else: 
        print ("Valor invalido, inicie novamente")