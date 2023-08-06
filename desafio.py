menu = """

[1] Depositar;
[2] Sacar;
[3] Extrato;
[q] Sair;

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
        # print("Deposito")
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excedeu o limite.")
        elif excedeu_saques:
            print("Operações falhou! Número máximo do saque excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        # print("Sacar")
    elif opcao == "3":
        print("\n********** EXTRATO **********")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"Total de saques realizados até o momento: {numero_saques:}")
        print("*********************************")
        # print("Extrato")
    elif opcao == "q":
        print("Sair! Muito obrigado pela preferência.")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejado.")
