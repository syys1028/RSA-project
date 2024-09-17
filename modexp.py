def modular_exponentiation(base, exponent, modulus):    # 거듭제곱 계산
    
    # (base ** exponent) % modulus

    result = 1
    base = base % modulus

    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2 
        base = (base * base) % modulus
    return result
