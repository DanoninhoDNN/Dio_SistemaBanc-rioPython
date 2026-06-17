print("Bem vindos ao ✧ Banco StarMax ✧ escolha uma opção a seguir")
MenuInicial = """

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR

"""
extrato = ""
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(MenuInicial)
    
    if opcao == "1":
        print ("Opção de deposito selecionada!")
        deposito = float(input("Digite o valor que desejá depositar: R$ "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            print(f"""A operação de deposito R${deposito:.2f} foi bem sucedida!
Seu saldo total é de R${saldo:.2f}
Deseja realizar mais alguma ação?: ) """)

    elif opcao == "2":
        print ("Opção de saque selecionada!")

        sacar = float(input("Digite o valor que desejá sacar: R$ "))
        #Arrumar aqui para que não quebre com letras
        #Arrumar para que não quebre com virgula
        excedeu_limite = sacar > limite
        excedeu_saldo = sacar > saldo
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print(f"Saldo informado indisponivel, seu saldo disponivel é de {saldo}!")

        elif  excedeu_saques:
            print("Operação falhou! Número máximo de saques diarios excedido.")
        
        elif excedeu_limite:
            print(f"Prezado, a limite de saque por tentativa é de {limite}")
        
        elif sacar > 0:
            saldo -= sacar
            extrato += f"Saque de R$: {sacar: .2f}\n"
            numero_saques += 1
            print(f"""A operação saque R${sacar:.2f} foi bem sucedida!
Seu saldo total é de R${saldo:.2f}
Deseja realizar mais alguma ação?: ) """)

        else: print("Favor inserir apenas valores numericos validos!")

    elif  opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")
    
    elif opcao == "0":
        print("✧ Banco StarMax agradece a preferencia ✧")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")