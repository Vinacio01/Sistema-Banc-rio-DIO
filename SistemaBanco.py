menu = """
========== MENU DO SISTEMA ==========
[s] Sacar
[d] Depósito
[e] Extrato
[q] Sair
=====================================
Escolha uma opção: """

saldo = 0                
limite = 500               
numero_saques = 0            
LIMITE_SAQUES = 3            
extrato = ""  

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input('Digite seu deposito: '))

        if valor > 0:
            saldo += valor
            extrato += (f'Depósito: R$ {valor:.2f}\n')

        else:
            print('Operação falhou, tente novamente')

    elif opcao == "s":
        valor = float(input('Qual o valor do saque: '))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print('Voce nao tens dinheiro suficiente para sacar.')
        elif excedeu_limite:
            print('o limite de saque é de 500 reais.')
        elif excedeu_saques:
            print('Voce sacou 3 vezes no dia, volte amanha ou fale com seu gerente.')
        elif valor > 0:
            saldo -= valor
            extrato += (f'Saquee: R$ {valor:.2f}\n')
            numero_saques += 1
        else:
            print('Operação invalida')

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================\n")

    elif opcao == "q":
        print('Voce saiu do sistema.')
        break

    else:
        print('Operação invalida, tente novamente.')