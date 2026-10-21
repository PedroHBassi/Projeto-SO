def simular_fifo(sequencia, quantidade_frames):
    if quantidade_frames < 1:
        raise ValueError("A quantidade de frames deve ser maior que zero.")
    frames = []
    proxima_substituicao = 0
    hits = faults = 0
    historico = []
    for pagina in sequencia:
        substituida = None
        if pagina in frames:
            resultado = "HIT"
            hits += 1
        else:
            resultado = "PAGE FAULT"
            faults += 1
            if len(frames) < quantidade_frames:
                frames.append(pagina)
            else:
                substituida = frames[proxima_substituicao]
                frames[proxima_substituicao] = pagina
                proxima_substituicao = (proxima_substituicao + 1) % quantidade_frames
        historico.append({
            "pagina": pagina,
            "frames": frames.copy(),
            "resultado": resultado,
            "substituida": substituida,
        })
    return {"algoritmo": "FIFO", "hits": hits, "faults": faults, "historico": historico}


def simular_lru(sequencia, quantidade_frames):
    if quantidade_frames < 1:
        raise ValueError("A quantidade de frames deve ser maior que zero.")
    frames = []
    ultima_utilizacao = {}
    hits = faults = 0
    historico = []
    for instante, pagina in enumerate(sequencia):
        substituida = None
        if pagina in frames:
            resultado = "HIT"
            hits += 1
        else:
            resultado = "PAGE FAULT"
            faults += 1
            if len(frames) < quantidade_frames:
                frames.append(pagina)
            else:
                pagina_lru = min(frames, key=lambda p: ultima_utilizacao[p])
                indice = frames.index(pagina_lru)
                substituida = frames[indice]
                frames[indice] = pagina
        ultima_utilizacao[pagina] = instante
        historico.append({
            "pagina": pagina,
            "frames": frames.copy(),
            "resultado": resultado,
            "substituida": substituida,
        })
    return {"algoritmo": "LRU", "hits": hits, "faults": faults, "historico": historico}


def exibir_resultado(resultado):
    print(f"\n--- {resultado['algoritmo']} ---")
    print(f"{'Passo':<6}{'Página':<9}{'Frames após acesso':<25}{'Resultado':<15}{'Substituição'}")
    print("-" * 75)
    for passo, item in enumerate(resultado["historico"], start=1):
        substituicao = str(item["substituida"]) if item["substituida"] is not None else "-"
        print(f"{passo:<6}{item['pagina']:<9}{str(item['frames']):<25}{item['resultado']:<15}{substituicao}")
    print(f"Hits: {resultado['hits']} | Page faults: {resultado['faults']} | Acessos: {resultado['hits'] + resultado['faults']}")


def sequencia_belady():
    return [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
