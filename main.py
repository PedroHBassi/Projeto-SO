from loja import LojaJogos


def ler_int(mensagem, minimo=None):
    while True:
        try:
            valor = int(input(mensagem).strip())
            if minimo is not None and valor < minimo:
                print(f"Digite um número maior ou igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def menu():
    loja = LojaJogos()
    while True:
        print("\n" + "=" * 54)
        print("       GAME STORE - SIMULADOR DE SISTEMAS OPERACIONAIS")
        print("=" * 54)
        print("1 - Ver catálogo de jogos")
        print("2 - Comprar jogo")
        print("3 - Ver pedidos aguardando estoque")
        print("4 - Processar próximo pedido")
        print("5 - Ver memória cache (FIFO)")
        print("6 - Ver memória cache (LRU)")
        print("7 - Comparar FIFO e LRU")
        print("8 - Demonstrar anomalia de Belady")
        print("9 - Simular deadlock no estoque")
        print("10 - Executar testes automáticos")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            loja.exibir_catalogo()
        elif opcao == "2":
            loja.comprar_jogo()
        elif opcao == "3":
            loja.exibir_pedidos()
        elif opcao == "4":
            loja.processar_pedido()
        elif opcao == "5":
            loja.exibir_cache("FIFO")
        elif opcao == "6":
            loja.exibir_cache("LRU")
        elif opcao == "7":
            loja.comparar_cache()
        elif opcao == "8":
            loja.demonstrar_belady()
        elif opcao == "9":
            loja.simular_deadlock()
        elif opcao == "10":
            from testes import executar_testes
            executar_testes()
        elif opcao == "0":
            print("Obrigado por visitar a Game Store!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
