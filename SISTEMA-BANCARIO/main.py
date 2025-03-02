import os

saldo = [0]

def consultar_saldo():
    os.system("clear")
    print("Consultando saldo...")
    print(f"Seu saldo é de R${saldo[0]}")

def depositar():
    os.system("clear")
    print("Depositando...")
    valor = float(input("Digite o valor a ser depositado: "))
    saldo[0] += valor
    print("Depósito realizado com sucesso!")

def sacar():
    os.system("clear")
    print("Sacando...")
    valor = float(input("Digite o valor a ser sacado: "))
    if saldo[0] >= valor:
        saldo[0] -= valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

def menu():
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

def main():
    print("Bem vindo ao Banco do Python!")
    menu()
    opcao = int(input("Digite a opção desejada: "))

    while opcao != 4:
        if opcao == 1:
            consultar_saldo()
        elif opcao == 2:
            depositar()
        elif opcao == 3:
            sacar()
        else:
            print("Opção inválida!")

        menu()
        opcao = int(input("Digite a opção desejada: "))

if __name__ == "__main__":
    main()