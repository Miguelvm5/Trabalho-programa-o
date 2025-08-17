import random

contas = []

TAXA_SAQUE = 1.50
TAXA_TRANSFERENCIA = 2.00

def cadastrar_conta():
    """Cadastra uma nova conta bancária"""
    print("\n--- Cadastro de Nova Conta ---")
    nome = input("Nome do cliente: ")
    senha = input("Crie uma senha: ")
    
    numero_conta = str(random.randint(100000, 999999))
    
    saldo_inicial = float(input("Saldo inicial: R$ "))

    conta = {
        'nome': nome,
        'numero_conta': numero_conta,
        'senha': senha,
        'saldo': saldo_inicial,
        'extrato': []
    }
    
    contas.append(conta)
    print(f"\nConta criada com sucesso! Número da conta: {numero_conta}")
    print(f"Saldo inicial: R$ {saldo_inicial:.2f}")

def login():
    print("\n--- Login ---")
    numero_conta = input("Número da conta: ")
    senha = input("Senha: ")
    
    for conta in contas:
        if conta['numero_conta'] == numero_conta and conta['senha'] == senha:
            print(f"\nBem-vindo, {conta['nome']}!")
            return conta
    
    print("\nNúmero da conta ou senha incorretos.")
    return None

def sacar(conta):
    print("\n--- Saque ---")
    valor = float(input("Valor a sacar: R$ "))
    
    if valor <= 0:
        print("Valor inválido para saque.")
        return
    
    total_debitado = valor + TAXA_SAQUE
    
    if conta['saldo'] >= total_debitado:
        conta['saldo'] -= total_debitado
        conta['extrato'].append(f"Saque: -R$ {valor:.2f} (Taxa: R$ {TAXA_SAQUE:.2f})")
        print(f"Saque realizado com sucesso! Saldo atual: R$ {conta['saldo']:.2f}")
    else:
        print("Saldo insuficiente para realizar o saque.")

def depositar(conta):
    print("\n--- Depósito ---")
    valor = float(input("Valor a depositar: R$ "))
    
    if valor <= 0:
        print("Valor inválido para depósito.")
        return
    
    conta['saldo'] += valor
    conta['extrato'].append(f"Depósito: +R$ {valor:.2f}")
    print(f"Depósito realizado com sucesso! Saldo atual: R$ {conta['saldo']:.2f}")

def transferir(conta_origem):
    print("\n--- Transferência ---")
    numero_destino = input("Número da conta destino: ")
    valor = float(input("Valor a transferir: R$ "))
    
    if valor <= 0:
        print("Valor inválido para transferência.")
        return
    
    total_debitado = valor + TAXA_TRANSFERENCIA

    conta_destino = None
    for conta in contas:
        if conta['numero_conta'] == numero_destino:
            conta_destino = conta
            break
    
    if not conta_destino:
        print("Conta destino não encontrada.")
        return
    
    if conta_origem['saldo'] >= total_debitado:

        conta_origem['saldo'] -= total_debitado
        conta_destino['saldo'] += valor
        
        conta_origem['extrato'].append(
            f"Transferência para {conta_destino['numero_conta']}: -R$ {valor:.2f} (Taxa: R$ {TAXA_TRANSFERENCIA:.2f})")
        conta_destino['extrato'].append(
            f"Transferência de {conta_origem['numero_conta']}: +R$ {valor:.2f}")
        
        print(f"Transferência realizada com sucesso! Saldo atual: R$ {conta_origem['saldo']:.2f}")
    else:
        print("Saldo insuficiente para realizar a transferência.")

def ver_saldo(conta):
    print("\n--- Saldo ---")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")

def ver_extrato(conta):
    print("\n--- Extrato ---")
    print(f"Extrato da conta {conta['numero_conta']} - {conta['nome']}")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}\n")
    
    if not conta['extrato']:
        print("Nenhuma operação realizada ainda.")
    else:
        for operacao in conta['extrato']:
            print(operacao)

def menu_principal():
    print("\n=== Sistema Bancário ===")
    print("1. Cadastrar nova conta")
    print("2. Acessar conta existente")
    print("3. Sair")
    return input("Escolha uma opção: ")

def menu_conta():
    print("\n=== Menu da Conta ===")
    print("1. Sacar")
    print("2. Depositar")
    print("3. Transferir")
    print("4. Ver saldo")
    print("5. Ver extrato")
    print("6. Sair da conta")
    return input("Escolha uma opção: ")

def main():
    
    while True:
        opcao = menu_principal()
        
        if opcao == "1":
            cadastrar_conta()
        elif opcao == "2":
            conta = login()
            if conta:
                while True:
                    opcao_conta = menu_conta()
                    
                    if opcao_conta == "1":
                        sacar(conta)
                    elif opcao_conta == "2":
                        depositar(conta)
                    elif opcao_conta == "3":
                        transferir(conta)
                    elif opcao_conta == "4":
                        ver_saldo(conta)
                    elif opcao_conta == "5":
                        ver_extrato(conta)
                    elif opcao_conta == "6":
                        print("Saindo da conta...")
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
        elif opcao == "3":
            print("Obrigado por usar nosso sistema bancário. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()