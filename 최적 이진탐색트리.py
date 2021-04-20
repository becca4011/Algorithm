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
    A = [[0 for j in range(n+1)] for i in range(n+2)] # 배열 생성 (5X6)
    """
      0 1 2 3 4
    1
    2
    3                이런식의 표로 되어있으므로 하나 크게 줌
    4
    5
    """

    for i in range(1, n+1): 
        A[i][i] = p[i-1] # (1, 1), (2, 2), (3, 3), ... 은 나와있는 확률로 채움
        R[i][i] = i # 최소치를 주는 값은 i (원래의 확률이므로)

    for diagonal in range(1, n+1):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal
            m = 10000

            for k in range(i, j+1):
                if m > A[i][k - 1] + A[k + 1][j] + round(sum(p[i-1:j]), 1): # m보다 작을 때 (m에는 작은 값 저장)
                    A[i][j] = A[i][k - 1] + A[k + 1][j] + round(sum(p[i-1:j]), 1) # A[i][j]에 값 넣기
                    m = A[i][j] # 작은 값 바꿔주기
                    R[i][j] = k # k가 최소치를 주는 값

    print("<A>")
    for i in A[1:]: # 배열을 하나 더 크게 해서 자르기
        print(i)

    print("\n<R>")
    for i in R[1:]:
        print(i)

optsrchtree(n, p, R)