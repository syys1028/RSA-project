from euclid import extended_gcd

def modular_inverse(a, n):  # 모듈러 역원을 계산합니다.

    # a * x ≡ 1 mod n

    gcd_value, x, _ = extended_gcd(a, n)
    if gcd_value != 1:
        return None  
    else:
        return x % n
