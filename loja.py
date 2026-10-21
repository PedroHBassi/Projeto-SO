from memoria import simular_fifo, simular_lru, exibir_resultado, sequencia_belady
from deadlock import detectar_deadlock


class LojaJogos:
    def __init__(self):
        self.catalogo = {
            1: {"nome": "GTA 6", "preco": 499.90, "estoque": 4, "plataforma": "PlayStation / Xbox"},
            2: {"nome": "EA Sports FC 27", "preco": 349.90, "estoque": 5, "plataforma": "PlayStation / Xbox / PC"},
            3: {"nome": "Minecraft", "preco": 119.90, "estoque": 8, "plataforma": "PC / Console"},
            4: {"nome": "Counter Strike 2", "preco": 89.90, "estoque": 3, "plataforma": "PC"},
            5: {"nome": "The Wither 3", "preco": 249.90, "estoque": 2, "plataforma": "PlayStation / Xbox / Switch / PC"},
            6: {"nome": "Cyberpunk 2077", "preco": 249.90, "estoque": 6, "plataforma": "PC / PlayStation / Xbox"},
        }
        self.pedidos = []
        self.acessos_produtos = []
        self.frames_cache = 3
        self.proximo_id_pedido = 1

    def exibir_catalogo(self):
        print("\n=== CATÁLOGO DE JOGOS ===")
        print(f"{'ID':<4}{'Jogo':<39}{'Preço':<12}{'Estoque':<10}Plataforma")
        print("-" * 100)
        for id_jogo, jogo in self.catalogo.items():
            print(f"{id_jogo:<4}{jogo['nome']:<39}R$ {jogo['preco']:<8.2f}{jogo['estoque']:<10}{jogo['plataforma']}")
        print("\nCada consulta de produto é registrada para simular acessos à memória cache.")

    def comprar_jogo(self):
        self.exibir_catalogo()
        try:
            id_jogo = int(input("\nDigite o ID do jogo desejado: ").strip())
        except ValueError:
            print("ID inválido.")
            return
        if id_jogo not in self.catalogo:
            print("Jogo não encontrado.")
            return

        jogo = self.catalogo[id_jogo]
        self.acessos_produtos.append(id_jogo)
        quantidade = self._ler_quantidade()
        if quantidade is None:
            return

        if jogo["estoque"] >= quantidade:
            jogo["estoque"] -= quantidade
            pedido = {
                "id": self.proximo_id_pedido,
                "jogo_id": id_jogo,
                "quantidade": quantidade,
                "total": jogo["preco"] * quantidade,
                "status": "Confirmado",
            }
            self.pedidos.append(pedido)
            self.proximo_id_pedido += 1
            print(f"Compra confirmada: {jogo['nome']} x{quantidade}. Total: R$ {pedido['total']:.2f}")
        else:
            pedido = {
                "id": self.proximo_id_pedido,
                "jogo_id": id_jogo,
                "quantidade": quantidade,
                "total": jogo["preco"] * quantidade,
                "status": "Aguardando estoque",
            }
            self.pedidos.append(pedido)
            self.proximo_id_pedido += 1
            print("Estoque insuficiente. Pedido colocado na fila de espera.")
            print("O pedido poderá ser processado quando houver estoque disponível.")

    def _ler_quantidade(self):
        try:
            quantidade = int(input("Quantidade: ").strip())
            if quantidade < 1:
                print("A quantidade deve ser maior que zero.")
                return None
            return quantidade
        except ValueError:
            print("Quantidade inválida.")
            return None

    def exibir_pedidos(self):
        print("\n=== PEDIDOS ===")
        if not self.pedidos:
            print("Ainda não há pedidos.")
            return
        for pedido in self.pedidos:
            jogo = self.catalogo[pedido["jogo_id"]]
            print(f"Pedido #{pedido['id']} | {jogo['nome']} | Qtde: {pedido['quantidade']} | "
                  f"Total: R$ {pedido['total']:.2f} | Status: {pedido['status']}")

    def processar_pedido(self):
        aguardando = next((p for p in self.pedidos if p["status"] == "Aguardando estoque"), None)
        if aguardando is None:
            print("Não há pedidos aguardando estoque.")
            return
        jogo = self.catalogo[aguardando["jogo_id"]]
        if jogo["estoque"] >= aguardando["quantidade"]:
            jogo["estoque"] -= aguardando["quantidade"]
            aguardando["status"] = "Confirmado"
            print(f"Pedido #{aguardando['id']} confirmado.")
        else:
            print(f"Pedido #{aguardando['id']} continua aguardando: estoque de {jogo['nome']} insuficiente.")
            print("Para testar o processamento, reduza a quantidade do pedido ou acrescente estoque no código.")

    def _registrar_consultas_demo(self):
        if not self.acessos_produtos:
            self.acessos_produtos = [1, 2, 3, 1, 4, 2, 5, 1, 2]
        return self.acessos_produtos

    def exibir_cache(self, algoritmo):
        sequencia = self._registrar_consultas_demo()
        funcao = simular_fifo if algoritmo == "FIFO" else simular_lru
        resultado = funcao(sequencia, self.frames_cache)
        exibir_resultado(resultado)
        print("Interpretação: cada número representa uma página de dados de produto consultada.")

    def comparar_cache(self):
        sequencia = self._registrar_consultas_demo()
        print("\n=== COMPARAÇÃO DA CACHE DA LOJA ===")
        print("Acessos registrados (IDs dos jogos):", sequencia)
        exibir_resultado(simular_fifo(sequencia, self.frames_cache))
        exibir_resultado(simular_lru(sequencia, self.frames_cache))

    def demonstrar_belady(self):
        sequencia = sequencia_belady()
        print("\n=== ANOMALIA DE BELADY NA CACHE ===")
        print("Sequência didática de páginas:", " ".join(map(str, sequencia)))
        for quantidade in (3, 4):
            resultado = simular_fifo(sequencia, quantidade)
            print(f"FIFO com {quantidade} frames: {resultado['faults']} page faults.")
        print("A sequência é um teste teórico do algoritmo de cache, não um histórico real de vendas.")

    def simular_deadlock(self):
        print("\n=== DEADLOCK NO PROCESSAMENTO DE PEDIDOS ===")
        print("Cenário simulado:")
        print("- Processo P1 (pedido de console) segura o recurso R1 (estoque reservado) e espera R2 (pagamento liberado).")
        print("- Processo P2 (pedido de jogo) segura R2 (pagamento reservado) e espera R1 (estoque liberado).")
        print("Esse cenário forma um ciclo de espera.")
        grafo = {"P1": ["P2"], "P2": ["P1"]}
        envolvidos = detectar_deadlock(grafo)
        if envolvidos:
            print("DEADLOCK DETECTADO entre:", ", ".join(envolvidos))
            print("Solução possível no sistema real: liberar reservas em ordem definida ou cancelar uma das operações.")
        else:
            print("Nenhum deadlock detectado.")
