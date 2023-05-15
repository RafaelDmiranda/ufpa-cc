# Cria uma lista vazia com 8 células
memoria = [0] * 8

# Função para imprimir a memória
def listar_memoria():
    for i in range(len(memoria)):
        endereco = format(i, '04b')
        valor = format(memoria[i], '08b')
        print(f"Célula {endereco}: {valor}")

# Loop principal do programa
while True:
    print("1 - Ler célula")
    print("2 - Escrever em célula")
    print("3 - Listar memória")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1": # Ler célula
        endereco = input("Digite o endereço da célula (0000 a 0111): ")
        if not all(digito in "01" for digito in endereco) or len(endereco) != 4:
            print("Endereço inválido!")
        else:
            endereco = int(endereco, 2)
            print(f"Valor na célula {endereco}: {format(memoria[endereco], '08b')}")

    elif opcao == "2": # Escrever em célula
        endereco = input("Digite o endereço da célula (0000 a 0111): ")
        if not all(digito in "01" for digito in endereco) or len(endereco) != 4:
            print("Endereço inválido!")
        else:
            endereco = int(endereco, 2)
            valor = input("Digite o valor binário a ser escrito (8 bits): ")
            if len(valor) != 8 or not all(digito in "01" for digito in valor):
                print("Valor inválido!")
            else:
                memoria[endereco] = int(valor, 2)
                print(f"Valor {valor} escrito na célula {format(endereco, '04b')}")

    elif opcao == "3": # Listar memória
        listar_memoria()

    elif opcao == "0": # Sair
        break

    else:
        print("Opção inválida!")