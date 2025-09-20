from KnapsackConstants import A_20, C_20, S_20

def knapsack_01(valores, pesos, capacidade):
    n = len(valores)
    dp = [0] * (capacidade + 1)


    guardar = [[0]*(capacidade+1) for _ in range(n+1)]

    for i in range(1, n+1):
        v, p = valores[i-1], pesos[i-1]
        for w in range(capacidade, p-1, -1):
            if dp[w-p] + v > dp[w]:
                dp[w] = dp[v-p] + v
                guardar[i][w] = 1

    valor_maximo = dp[capacidade]


    escolha = []
    w = capacidade
    for i in range(n, 0, -1):
        if guardar[i][w] == 1:
            escolha.append(i-1)
            w -= pesos[i-1]

    escolha.reverse()
    return valor_maximo, escolha


if __name__ == "__main__":
    valor_max, items = knapsack_01(A_20, C_20, S_20)
    print("Valor máximo:", valor_max)
    print("Itens escolhidos:", items)
