from prime import generate_prime
from modexp import modular_exponentiation
from inverse import modular_inverse
from euclid import gcd

class RSA:
    def __init__(self, bits=1024):  # RSA 키를 초기화
        self.e = 65537  # 일반적으로 사용되는 공개 지수
        self.bits = bits
        self.generate_keys()

    def generate_keys(self):  #공개키, 비밀키를 생성
        p = generate_prime(self.bits)
        q = generate_prime(self.bits)
        while q == p:
            q = generate_prime(self.bits)

        self.n = p * q
        phi = (p - 1) * (q - 1)

        if gcd(self.e, phi) != 1:
            raise ValueError("e와 φ(n)은 서로소여야 합니다.")

        self.d = modular_inverse(self.e, phi)
        if self.d is None:
            raise ValueError("d의 모듈러 역원을 계산할 수 없습니다.")

    def encrypt(self, plaintext):   # 평문 암호화
        return modular_exponentiation(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):  # 암호문 복호화
        return modular_exponentiation(ciphertext, self.d, self.n)
