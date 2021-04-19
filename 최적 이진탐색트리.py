n = 4
p = [0.1, 0.3, 0.4, 0.2]

R = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ]

def optsrchtree(n, p, R):
    A = [[0 for j in range(n+1)] for i in range(n+2)]

    for i in range(1, n+1):
        A[i][i] = p[i-1]
        R[i][i] = i

    for diagonal in range(1, n+1):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            m = 10000

            for k in range(i, j+1):
                if m > A[i][k - 1] + A[k + 1][j] + round(sum(p[i-1:j]), 1):
                    #print(A[i][k - 1] + A[k + 1][j] + round(sum(p[i-1:j]), 1))
                    A[i][j] = A[i][k - 1] + A[k + 1][j] + round(sum(p[i-1:j]), 1)
                    m = A[i][j]
                    R[i][j] = k

    print("<A>")
    for i in A[1:]:
        print(i)

    print("\n<R>")
    for i in R[1:]:
        print(i)

optsrchtree(n, p, R)