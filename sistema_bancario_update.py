saldo = 0
extrato = ""
cadastro_usuario = {}

while True:
    print("\nO que você gostaria de fazer?")
    print("[c] Criar conta bancaria")
    print("[d] Depositar")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")
    opcao = input("Escolha uma opção: ").lower()

    if opcao == 'c':

        nome_completo = input("Nome Completo: ")
        endereco = input("Endereço: ")
        data_nascimento = input("Data de Nascimento: ")
        cpf = input("CPF: ")
        cadastro_usuario = {
            "Nome completo": nome_completo,
            "Endereço": endereco,
            "Data de Nascimento": data_nascimento,
            "CPF": cpf
        }

        print("conta bancária criada com sucesso!")

    if opcao == 'd':

        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("O valor precisa ser positivo!")

    elif opcao == 's':

        valor = float(input("Informe o valor do saque: "))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido ou saldo insuficiente!")

    elif opcao == 'e':

        print("\n===== EXTRATO =====")
        if extrato == "":
            print("Nenhuma operação foi realizada.")
        else:
            print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===================")

    elif opcao == 'q':

        print("Obrigado por usar nosso serviço!")
        break

    else:

        print("Opção inválida! Por favor, tente novamente.")
