# W = [
#     [0, 1, 99, 1, 5],
#     [9, 0, 3, 2, 99],
#     [99, 99, 0, 4, 99],
#     [99, 99, 2, 0, 3],
#     [3, 99, 99, 99, 0]
#     ]

# P = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0]
#     ]

W = [
    [0, 2, 6, 99],
    [5, 0, 2, 3],
    [6, 99, 0, 4],
    [1, 99, 7, 0]
    ]

P = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]

# W = [
#     [0, 2, 9, 99],
#     [1, 0, 6, 4],
#     [99, 7, 0, 8],
#     [6, 3, 99, 0]
#     ]

# P = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
#     ]

def floyd(n, W, D, P):
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    P[i][j] = k + 1
                    D[i][j] = D[i][k] + D[k][j]

    print("<D5>")
    for i in range(n):
        print(D[i])

    print("\n<P5>")
    for i in range(n):
        print(P[i])

def path(q, r):
    #print(q, r)
    if q > 0:
        q = q - 1
    if r > 0:
        r = r - 1

    if P[q][r] != 0:
        path(q + 1, P[q][r])
        print("v%d" % P[q][r], end=" ")
        path(P[q][r], r + 1)

floyd(4, W, W, P)

print("\n<Path>\nv4", end=" ")
path(4, 3)
print("v3")