def text_to_int(text):  #텍스트를 정수로 변환
    return int.from_bytes(text.encode('utf-8'), byteorder='big')

def int_to_text(number):    #정수를 텍스트로 변환
    byte_length = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_length, byteorder='big').decode('utf-8', errors='ignore')
