def simular_fifo(sequencia, quantidade_frames):
    # Verifica se existe pelo menos um frame disponível.
    if quantidade_frames < 1:
        raise ValueError("A quantidade de frames deve ser maior que zero.")

    # sequencia é a lista de páginas que o programa vai solicitar
    # quantidade_frames é a quantidade de quadros disponíveis para armazenar páginas na memória simulada

    frames = [] # Cria uma lista vazia para guardar as páginas que estão atualmente na memória
    proxima_substituicao = 0 # Indica a posição do quadro que será substituído quando a memória estiver cheia
    hits = faults = 0 # Inicializa os contadores de acertos e faltas de página em zero.
    historico = [] # Guarda os resultados de cada acesso à memória


     # Percorre cada página da sequência na ordem em que foi solicitada.
    for pagina in sequencia:
        substituida = None  # Indica que nenhuma página foi substituída inicialmente.

        # Se a página já estiver na memória, não precisa substituir nada.
        if pagina in frames:
            resultado = "HIT"
            hits += 1
        else:
            # Se a página não estiver na memória, ocorre uma falta de página.
            resultado = "PAGE FAULT"
            faults += 1

            if len(frames) < quantidade_frames:
                # Se ainda houver espaço, adiciona a página sem remover outra.
                frames.append(pagina)
            else:
                # Se a memória estiver cheia, seleciona a página mais antiga.
                substituida = frames[proxima_substituicao]
                 # Coloca a nova página no lugar da página selecionada.
                frames[proxima_substituicao] = pagina

                 # Avança para a próxima posição de substituição.
                proxima_substituicao = (proxima_substituicao + 1) % quantidade_frames

        # Guarda o estado da memória após cada acesso.
        historico.append({
            "pagina": pagina, # Página que foi solicitada.
            "frames": frames.copy(), # Guarda uma cópia dos frames para preservar o estado de cada etapa.
            "resultado": resultado, # Indica se ocorreu HIT ou PAGE FAULT.
            "substituida": substituida, # Página removida, caso tenha ocorrido substituição.
        })

    return {
        "algoritmo": "FIFO",  # Nome do algoritmo utilizado.
        "hits": hits, # Total de acertos na memória.
        "faults": faults, # Total de faltas de página.
        "historico": historico # Histórico de todas as etapas da simulação.
    }


def simular_lru(sequencia, quantidade_frames):
    # Evita executar a simulação sem frames disponíveis.
    if quantidade_frames < 1:
        raise ValueError("A quantidade de frames deve ser maior que zero.")

    frames = []  # Guarda as páginas que estão atualmente na memória.
    ultima_utilizacao = {}  # Registra o último acesso de cada página.
    hits = faults = 0  # Inicializa os contadores de acertos e faltas de página.
    historico = []  # Armazena os resultados de cada etapa da simulação.

    
    for instante, pagina in enumerate(sequencia):
        substituida = None

        if pagina in frames:
            # A página já está carregada, então ocorre um HIT.
            resultado = "HIT"
            hits += 1
        else:
            resultado = "PAGE FAULT"
            faults += 1

            if len(frames) < quantidade_frames:
                # Se houver espaço livre, não é necessário substituir.
                frames.append(pagina)
            else:
                # Encontra a página que está há mais tempo sem ser acessada.
                pagina_lru = min(frames, key=lambda p: ultima_utilizacao[p])
                indice = frames.index(pagina_lru)

                substituida = frames[indice]
                frames[indice] = pagina

        # Atualiza o instante do último acesso à página.
        ultima_utilizacao[pagina] = instante

        # Salva o estado da memória para consultar cada etapa depois.
        historico.append({
            "pagina": pagina,
            "frames": frames.copy(),
            "resultado": resultado,
            "substituida": substituida,
        })

    return {
        "algoritmo": "LRU",
        "hits": hits,
        "faults": faults,
        "historico": historico
    }


def exibir_resultado(resultado):
    # Mostra o nome do algoritmo e os títulos das colunas.
    print(f"\n--- {resultado['algoritmo']} ---")
    print(f"{'Passo':<6}{'Página':<9}{'Frames após acesso':<25}{'Resultado':<15}{'Substituição'}")
    print("-" * 75)

    # Percorre o histórico e exibe o que aconteceu em cada acesso.
    for passo, item in enumerate(resultado["historico"], start=1):
        substituicao = str(item["substituida"]) if item["substituida"] is not None else "-"

        print(f"{passo:<6}{item['pagina']:<9}{str(item['frames']):<25}{item['resultado']:<15}{substituicao}")

    # Apresenta o total de acertos, faltas de página e acessos.
    print(
        f"Hits: {resultado['hits']} | "
        f"Page faults: {resultado['faults']} | "
        f"Acessos: {resultado['hits'] + resultado['faults']}"
    )


def sequencia_belady():
    # Sequência de páginas usada para testar os algoritmos.
    return [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5],



