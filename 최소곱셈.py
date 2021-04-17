d = [5, 2, 3, 4, 6, 7, 8]
P = [[0 for j in range(6)] for i in range(6)]

def minmult(n, d, P):
    k = 0
    M = [[0 for j in range(n)] for i in range(n)]

    for diagonal in range(n):
        for i in range(n - diagonal):
            j = i + diagonal
            m = 10000 # 작은 값 검사하기
            for k in range(i, j):
                if m > M[i][k] + M[k+1][j] + d[i] * d[k+1] * d[j+1]:
                    M[i][j] = M[i][k] + M[k+1][j] + d[i] * d[k+1] * d[j+1]
                    m = M[i][j]
                    P[i][j] = k + 1

    return M[0][n - 1]

print(minmult(6, d, P))