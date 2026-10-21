def detectar_deadlock(grafo_espera):
    estado = {}
    pilha = []
    envolvidos = set()

    def dfs(processo):
        estado[processo] = 1
        pilha.append(processo)
        for vizinho in grafo_espera.get(processo, []):
            if estado.get(vizinho, 0) == 0:
                dfs(vizinho)
            elif estado.get(vizinho) == 1:
                inicio = pilha.index(vizinho)
                envolvidos.update(pilha[inicio:])
        pilha.pop()
        estado[processo] = 2

    todos = set(grafo_espera)
    for destinos in grafo_espera.values():
        todos.update(destinos)
    for processo in todos:
        if estado.get(processo, 0) == 0:
            dfs(processo)
    return sorted(envolvidos)

