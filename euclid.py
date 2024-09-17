def gcd(a, b):  # 유클리드 알고리즘으로 최대공약수를 계산

    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b): # 확장된 유클리드 알고리즘

    # ax + by = gcd(a, b)

    if b == 0:
        return a, 1, 0
    else:
        gcd_value, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd_value, x, y
