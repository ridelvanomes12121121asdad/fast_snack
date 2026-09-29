#variaveis para armazenar a quantidade de cada item do pedido
quantidade_hamburguer = 0
quantidade_batata = 0
quantidade_refrigerante = 0

#menu principal do sistema

while True:
    print("=== FAST SNACK ===")
    print("--- MENU PRINCIPAL ---")
    print("1 - NOVO PEDIDO")
    print("2 - CONSULTAR PEDIDO")
    print("3 - ENCERRAR PEDIDO")

    escolha = int(input("selecione a opcao: "))

    if escolha == 1:
        print("=== NOVO PEDIDO ===")
        print("1 - HAMBURGUER")
        print("2 - BATATA FRITA")
        print("3 - REFRIGERANTE")
        pedido = int(input("selecione o pedido (1, 2 ou 3): "))

        if pedido in (1, 2, 3):
            quantidade = int(input("selecione a quantidade: "))
            if pedido == 1:
                quantidade_hamburguer += quantidade
                print("Hamburguer selecionado!")
            elif pedido == 2:
                quantidade_batata += quantidade
                print("Batata frita selecionada!")
            else:
                quantidade_refrigerante += quantidade
                print("Refrigerante selecionado!")
        else:
            print("Opcao invalida!")
    elif escolha == 2:
        print("=== CONSULTAR PEDIDO ===")
        print(f"Quantidade de hamburguer: {quantidade_hamburguer}")
        print(f"Quantidade de batata frita: {quantidade_batata}")
        print(f"Quantidade de refrigerante: {quantidade_refrigerante}")
    elif escolha == 3:
        print("=== ENCERRAR PEDIDO ===")
        print("PEDIDO FINALIZADO COM SUCESSO")
        break
    else:
        print("Opcao invalida!")
