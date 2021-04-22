S = [15, 22, 13, 27, 12, 10, 20, 25]
pivotpoint = 0

def partition(low, high):
    global pivotpoint
    
    pivotitem = S[low]
    j = low

    for i in range(low, high):
        if S[i] < pivotitem:
            j += 1
            # pivotitem보다 작은 값이면 자리 바꾸기
            S[i], S[j] = S[j], S[i]
    
    pivotpoint = j
    # pivotitem과 pivotitem보다 작은 값 중 가장 오른쪽에 있는 값 바꾸기
    S[low], S[pivotpoint] = S[pivotpoint], S[low]

def quicksort(low, high):
    if high > low:
        partition(low, high)
        quicksort(low, pivotpoint)
        quicksort(pivotpoint + 1, high)

quicksort(0, 8)
print(S)