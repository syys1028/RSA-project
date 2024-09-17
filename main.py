from rsa import RSA
from text_conversion import text_to_int, int_to_text

while True:
    # RSA 객체 생성 (키 : 512비트)
    rsa = RSA(bits=512)

    # 메시지 입력
    message = input("\n암호화할 메시지를 입력하세요: ")
    print(f"\n원본 메시지: {message}")

    # 메시지를 정수로 변환
    message_int = text_to_int(message)

    # 암호화
    encrypted_int = rsa.encrypt(message_int)
    print(f"암호화된 메시지(정수): {encrypted_int}")

    # 복호화
    decrypted_int = rsa.decrypt(encrypted_int)

    # 정수를 텍스트로 변환
    decrypted_message = int_to_text(decrypted_int)
    print(f"복호화된 메시지: {decrypted_message}")
    
    # 복호화가 원본과 동일한지 확인
    if message == decrypted_message:
        print("암호화 및 복호화 성공!")
    else:
        print("원본 메시지와 일치하지 않습니다.")