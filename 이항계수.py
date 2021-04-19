def bin(n, k):
    B = [[0 for j in range(k + 1)] for i in range(n)]
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                B[i - 1][j] = 1
            else:
                B[i - 1][j] = B[i - 2][j - 1] + B[i - 2][j]

    return B[n - 1][k]

a, b = map(int, input("a, b입력 : ").split())
print(bin(a, b)) 