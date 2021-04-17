S = [27, 10, 12, 20, 25, 13, 15, 22]

def merge(h, m, U, V, S):
    i = j = k = 0
    while(i <= h - 1 and j <= m - 1):
        if U[i] < V[j]:
            S[k] = U[i]
            i += 1
        else:
            S[k] = V[j]
            j += 1
        k += 1
    if i > h - 1:
        S[k:h+m] = V[j:m]
    else:
        S[k:h+m] = U[i:m]

    print("merge     | S :", S)

def mergesort(n, S):
    h = n // 2
    m = n - h
    U = list()
    V = list()

    if n > 1:
        U = S[0:h] # S[0] ~ S[h-1] = U[0] ~ U[h-1]
        V = S[h:n] # S[h] ~ S[n-1] = V[0] ~ V[m-1]
        print("mergesort | U :", U, "/ V :", V)
        
        mergesort(h, U)
        mergesort(m, V)
        merge(h, m, U, V, S)

mergesort(8, S)
print(S)