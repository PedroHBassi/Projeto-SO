# 🎮 Projeto-SO — Loja de Jogos Eletrônicos

## 📌 Sobre o projeto

Este projeto foi desenvolvido em Python para a disciplina de **Sistemas Operacionais**. Ele simula o funcionamento de uma loja de jogos eletrônicos e demonstra conceitos importantes relacionados ao gerenciamento de memória e à sincronização de processos.

A aplicação permite visualizar jogos, realizar compras, controlar o estoque e gerenciar pedidos que aguardam reposição.

## 🎯 Objetivos

- Simular o funcionamento de uma loja de jogos eletrônicos.
- Implementar algoritmos de substituição de páginas.
- Comparar os algoritmos FIFO e LRU.
- Demonstrar a anomalia de Belady.
- Simular e detectar situações de deadlock.
- Realizar testes automáticos para verificar os resultados.

## ⚙️ Funcionalidades

- **Catálogo de jogos:** exibe jogos, preços, plataformas e quantidades em estoque.
- **Sistema de compras:** permite comprar jogos e atualiza o estoque.
- **Pedidos pendentes:** registra pedidos que aguardam disponibilidade de estoque.
- **FIFO:** substitui primeiro a página que entrou primeiro na memória.
- **LRU:** substitui a página que está há mais tempo sem ser utilizada.
- **Anomalia de Belady:** compara a quantidade de faltas de página com diferentes números de quadros.
- **Detecção de deadlock:** identifica ciclos de espera entre processos.
- **Testes automáticos:** verifica o funcionamento das principais funcionalidades.

## 🧠 Conceitos de Sistemas Operacionais

### FIFO (First In, First Out)

O primeiro elemento inserido é o primeiro a ser removido. No gerenciamento de memória, o algoritmo substitui a página mais antiga.

### LRU (Least Recently Used)

Substitui a página que está há mais tempo sem ser utilizada, considerando o histórico recente de acessos.

### Anomalia de Belady

É uma situação em que aumentar o número de quadros de memória pode aumentar a quantidade de faltas de página no algoritmo FIFO.

### Deadlock

É uma situação de impasse em que processos ficam esperando recursos uns dos outros, impedindo que continuem sua execução.

## 🛠️ Tecnologias utilizadas

- Python 3
- Programação orientada a objetos
- Estruturas de dados
- Algoritmos de substituição de páginas
- Testes automatizados

## ▶️ Como executar

**1.** Instale o Python 3, caso ainda não esteja instalado.

**2.** Abra o terminal na pasta do projeto.

**3.** Execute o programa:

```bash
python main.py
```

**4.** Para executar os testes automáticos:

```bash
python testes.py
```

## 📁 Estrutura do projeto

```text
Projeto-SO/
├── main.py       # Menu principal
├── loja.py       # Catálogo, compras e estoque
├── memoria.py    # Algoritmos FIFO e LRU
├── deadlock.py   # Detecção de deadlock
├── testes.py     # Testes automatizados
└── README.md     # Documentação do projeto
```

## 🧪 Testes

O projeto possui testes automatizados para verificar os algoritmos FIFO e LRU, a detecção de deadlock e a validação da quantidade de quadros de memória.

Na versão testada, **7 testes foram aprovados**.

## ⚠️ Limitações

Esta é uma simulação educacional. Os dados da loja permanecem em memória durante a execução e não são armazenados permanentemente em um banco de dados. Os algoritmos de memória e o deadlock são simulados, não representando o gerenciamento real de memória ou processos do sistema operacional.

## 👨‍💻 Disciplina

**Disciplina:** Sistemas Operacionais  
**Linguagem:** Python  
**Projeto:** Simulação de uma loja de jogos eletrônicos e conceitos de Sistemas Operacionais


## Simulação e solução de deadlock

A opção 9 demonstra um ciclo de espera entre P1 e P2. Em seguida, simula a recuperação cancelando a operação P2, removendo suas esperas e verificando que o ciclo desapareceu. Essa recuperação é didática: não cancela pedidos reais nem controla processos do sistema operacional.
