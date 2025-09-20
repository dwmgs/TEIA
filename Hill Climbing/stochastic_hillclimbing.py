import random
import numpy as np
import matplotlib.pyplot as plt
from KnapsackConstants import A_20, C_20, S_20


ganhos = A_20
custos = C_20
capacidade = S_20


def avaliar(solucao, ganhos, custos, capacidade):
    valor_total = sum(v for v, s in zip(ganhos, solucao) if s == 1)
    peso_total = sum(w for w, s in zip(custos, solucao) if s == 1)
    if peso_total > capacidade:
        return 0 
    return valor_total


def gerar_solucao_inicial(n, custos, capacidade):
    solucao = [0] * n
    indices = list(range(n))
    random.shuffle(indices)
    peso_atual = 0
    for i in indices:
        if peso_atual + custos[i] <= capacidade:
            solucao[i] = 1
            peso_atual += custos[i]
    return solucao


def vizinho(solucao):
    nova = solucao.copy()
    idx = random.randrange(len(solucao))
    nova[idx] = 1 - nova[idx]
    return nova


def hill_climbing(ganhos, custos, capacidade, max_iteracoes=1000):
    n = len(ganhos)
    atual = gerar_solucao_inicial(n, custos, capacidade)
    fitness_atual = avaliar(atual, ganhos, custos, capacidade)

    for _ in range(max_iteracoes):
        candidato = vizinho(atual)
        fitness_candidato = avaliar(candidato, ganhos, custos, capacidade)
        if fitness_candidato > fitness_atual:
            atual, fitness_atual = candidato, fitness_candidato
    return fitness_atual


def stochastic_hill_climbing(ganhos, custos, capacidade, max_iteracoes=1000):
    n = len(ganhos)
    atual = gerar_solucao_inicial(n, custos, capacidade)
    fitness_atual = avaliar(atual, ganhos, custos, capacidade)

    for _ in range(max_iteracoes):
        candidato = vizinho(atual)
        fitness_candidato = avaliar(candidato, ganhos, custos, capacidade)

        if fitness_candidato > fitness_atual and random.random() < 0.7:
            atual, fitness_atual = candidato, fitness_candidato

    return fitness_atual


resultados_tradicional = [hill_climbing(ganhos, custos, capacidade) for _ in range(30)]
resultados_estocastico = [stochastic_hill_climbing(ganhos, custos, capacidade) for _ in range(30)]


print("Hill Climbing Tradicional - Média Fitness:", np.mean(resultados_tradicional), "Desvio Padrão:", np.std(resultados_tradicional))
print("Stochastic Hill Climbing - Média Fitness:", np.mean(resultados_estocastico), "Desvio Padrão:", np.std(resultados_estocastico))


plt.boxplot([resultados_tradicional, resultados_estocastico], labels=["Tradicional", "Estocástico"])
plt.title("Comparação Hill Climbing vs Stochastic Hill Climbing")
plt.ylabel("Fitness")
plt.show()

