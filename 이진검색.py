S = [10, 12, 13, 14, 18, 20, 25, 27, 30, 35, 40, 45, 47]

x = int(input("입력 : "))

def binary(low, high):
    mid = (low + high) // 2
    if x == S[mid]:
        return mid
    elif x < S[mid]:
        return binary(low, mid - 1)
    else:
        return binary(mid + 1, high)

print(binary(0, 12), "번째") # 위치