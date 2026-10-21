from memoria import simular_fifo, simular_lru, sequencia_belady
from deadlock import detectar_deadlock


def executar_testes():
    casos = []
    seq = sequencia_belady()
    casos.append(("FIFO com 3 frames produz 9 faults", simular_fifo(seq, 3)["faults"] == 9))
    casos.append(("FIFO com 4 frames produz 10 faults", simular_fifo(seq, 4)["faults"] == 10))
    for nome, funcao in (("FIFO", simular_fifo), ("LRU", simular_lru)):
        r = funcao([1, 2, 1], 2)
        casos.append((f"{nome} conta 1 hit e 2 faults", r["hits"] == 1 and r["faults"] == 2))
    casos.append(("Detecta deadlock em ciclo", detectar_deadlock({"P1": ["P2"], "P2": ["P1"]}) == ["P1", "P2"]))
    casos.append(("Não detecta deadlock sem ciclo", detectar_deadlock({"P1": ["P2"], "P2": []}) == []))
    try:
        simular_fifo([1, 2], 0)
        casos.append(("Rejeita zero frames", False))
    except ValueError:
        casos.append(("Rejeita zero frames", True))

    print("\n=== TESTES AUTOMÁTICOS ===")
    aprovados = 0
    for nome, passou in casos:
        print(f"[{'OK' if passou else 'FALHOU'}] {nome}")
        aprovados += int(passou)
    print(f"Resultado: {aprovados}/{len(casos)} testes aprovados.")
    return aprovados == len(casos)


if __name__ == "__main__":
    executar_testes()
