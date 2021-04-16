S = [15, 22, 13, 27, 12, 10, 20, 25]
pivotpoint = 0

def partition(low, high, pivotpoint):
    pivotitem = S[low]
    j = low

    for i in range(low, high):
        if S[i] < pivotitem:
            j += 1
            temp = S[i]
            S[i] = S[j]
            S[j] = temp
    
    pivotpoint = j
    temp = S[low]
    S[low] = S[pivotpoint]
    S[pivotpoint] = temp

def quicksort(low, high):
    if high > low:
        partition(low, high, pivotpoint)
        quicksort(low, pivotpoint - 1)
        #quicksort(pivotpoint + 1, high) # 이게 있는 이유? (없어야 가능함)

quicksort(0, 8)
print(S)