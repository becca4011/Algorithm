S = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45, 47] # 정렬된 배열

x = int(input("입력 : "))

def binary(low, high):
    mid = (low + high) // 2
    if x == S[mid]: # 찾는 값과 mid 값이 같을 경우
        return mid
    elif x < S[mid]: # 찾는 값이 mid 값보다 작은 경우
        return binary(low, mid - 1) # mid 값보다 작으므로 찾는 값이 더 왼쪽에 있음
    else: # 찾는 값이 mid 값보다 큰 경우
        return binary(mid + 1, high) # mid 값보다 크므로 찾는 값이 더 오른쪽에 있음

print(binary(0, 12), "번째") # 위치