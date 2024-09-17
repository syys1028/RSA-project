import random
from modexp import modular_exponentiation

def is_prime(n, k=40):  # 밀러-라빈 소수 판정법
    
    if n <= 1:              # n이 소수인지 검사
        return False
    if n <= 3:
        return True

    if n % 2 == 0:
        return False
    
    r, d = 0, n - 1         # n - 1 = 2^r * d 형태로 변환
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = modular_exponentiation(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = modular_exponentiation(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):   # 소수를 생성
    while True:     # 홀수 후보 생성
        candidate = random.getrandbits(bits) | (1 << bits - 1) | 1
        if is_prime(candidate):
            return candidate
