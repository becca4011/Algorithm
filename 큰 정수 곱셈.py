import math

def prod(u, v):
    n = max(len(str(u)), len(str(v)))
    if u == 0 or v == 0:
        return 0
    elif n <= 5:
        print("u :", u, "/ v :", v, "/ u * v :", u * v)
        return u * v
    else:
        m = math.floor(n / 2)
        x = u // (10 ** m)
        y = u % (10 ** m)
        w = v // (10 ** m)
        z = v % (10 ** m)
        
        return prod(x, w) * (10 ** (2*m)) + (prod(x, z) + prod(w, y)) * (10 ** m) + prod(y, z)
        # 567 * 9423 * 10^6 + (567 * 723 + 9423 * 832) * 10^3 + 832 * 723

print(prod(567832, 9423723))