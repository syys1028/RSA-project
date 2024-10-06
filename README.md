# RSA-project
💡 [ Protfolio Project 004] RSA 알고리즘 구현 프로젝트 

## 📌 프로젝트 소개
이 프로젝트는 Python을 사용하여 RSA 암호화 알고리즘을 구현한 프로그램입니다. 사용자는 텍스트 메시지를 입력하면 프로그램이 해당 메시지를 RSA 알고리즘을 사용해 암호화 및 복호화합니다. 프로젝트는 주로 공개키 암호화를 학습하기 위해 만들어졌으며, 기본적인 RSA 암호화와 복호화 과정을 직접 구현합니다.  

## 📌 폴더 구조
    📂 RSA-project
    ┣ 📜 euclid.py                      # 확장 유클리드 알고리즘 구현 파일
    ┣ 📜 inverse.py                     # 모듈러 역원 계산 파일
    ┣ 📜 main.py                        # 프로그램 실행 및 RSA 암호화/복호화 처리 메인 파일
    ┣ 📜 modexp.py                      # 모듈러 지수 연산 구현 파일
    ┣ 📜 prime.py                       # 소수 생성 및 밀러-라빈 소수 판정법 구현 파일
    ┣ 📜 rsa.py                         # RSA 알고리즘 구현 파일 (키 생성, 암호화, 복호화)
    ┣ 📜 text_conversion.py             # 텍스트와 정수 변환 기능 구현 파일

## 📌 주요 기능
### - 키 생성 (Key Generation):
큰 소수 두 개를 생성한 뒤, 이를 사용하여 RSA의 공개키와 개인키를 생성합니다. 밀러-라빈 소수 판정법을 사용하여 소수 생성의 효율성을 높였습니다.  

### - 암호화 (Encryption): 
사용자가 입력한 평문을 RSA 공개키를 사용해 암호문으로 변환합니다. 텍스트 메시지를 정수로 변환한 후, RSA 수식을 통해 암호화 작업을 수행합니다.  

### - 복호화 (Decryption):
암호화된 메시지를 RSA 개인키를 통해 복호화하여 원본 메시지를 복원합니다. 암호문을 다시 정수로 변환한 후, RSA 수식을 통해 원래 평문으로 되돌립니다.  

### - 모듈러 지수 연산 (Modular Exponentiation):
암호화 및 복호화에서 큰 수를 다루기 위해 모듈러 지수 연산 알고리즘을 사용해 효율적인 계산을 구현합니다.  

### - 확장 유클리드 알고리즘 (Extended Euclidean Algorithm):
RSA에서 필요한 **GCD (최대 공약수)**와 모듈러 역원 계산을 위해 확장 유클리드 알고리즘을 사용했습니다.  

## 📌 구현 상세
### - RSA 암호화 알고리즘:
공개키 암호화 알고리즘으로, 두 소수의 곱을 기반으로 한 수학적 문제를 사용하여 암호화 및 복호화를 수행합니다.  

### - 밀러-라빈 소수 판정법:
큰 소수를 효율적으로 찾기 위한 확률적 소수 판별 알고리즘입니다. 이 알고리즘을 통해 큰 소수를 선택하여 RSA의 보안을 높입니다.  

### - 모듈러 지수 연산 (Modular Exponentiation):
RSA 암호화 및 복호화에서 큰 수의 거듭제곱을 모듈 연산으로 계산하기 위한 효율적인 알고리즘입니다.  

### - 확장 유클리드 알고리즘 (Extended Euclidean Algorithm):
두 정수의 최대 공약수를 구하는 유클리드 알고리즘을 확장하여 모듈러 역원 계산에 사용됩니다. RSA 알고리즘에서 중요한 개인키(d) 값을 계산할 때 사용됩니다.  

## 📌 개발 환경
  Python  
  PyCharm  
