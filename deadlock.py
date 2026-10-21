def detectar_deadlock(grafo_espera):
    """Retorna os processos envolvidos em ciclos do grafo de espera."""
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


def resolver_deadlock(grafo_espera, processo_vitima=None):
    """Simula a recuperação cancelando um processo envolvido e suas esperas.

    Retorna o grafo após a recuperação e o processo cancelado.
    É uma simulação didática: não encerra processos reais do sistema.
    """
    grafo = {p: list(destinos) for p, destinos in grafo_espera.items()}
    envolvidos = detectar_deadlock(grafo)
    if not envolvidos:
        return grafo, None

    if processo_vitima not in envolvidos:
        processo_vitima = envolvidos[-1]

    # Cancelar a operação vítima libera seus recursos simulados e remove
    # suas esperas; outros processos deixam de esperar por ela.
    grafo.pop(processo_vitima, None)
    for destinos in grafo.values():
        while processo_vitima in destinos:
            destinos.remove(processo_vitima)
    return grafo, processo_vitima

