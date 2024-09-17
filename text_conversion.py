def text_to_int(text):  #�ؽ�Ʈ�� ������ ��ȯ
    return int.from_bytes(text.encode('utf-8'), byteorder='big')

def int_to_text(number):    #������ �ؽ�Ʈ�� ��ȯ
    byte_length = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_length, byteorder='big').decode('utf-8', errors='ignore')
