# 2주차 1차시 강의교안 13페이지 코드

if __name__ == '__main__':
    # Decode
    # Translating from the outside world of bytes to Unicode Characters
    input_bytes = b'\xff\xfe4\x001\x003\x00 \x00i\x00s\x00 \x00i\x00n\x00.\x00'
    input_characters = input_bytes.decode('utf-16')
    print(repr(input_characters))

    # Encode
    # Translating characters back into bytes before sending them.
    output_characters = 'We copy you down, Eagle.\n'
    output_bytes = output_characters.encode('utf-8')
    with open('Network/eagle.txt', 'wb') as f:
        f.write(output_bytes) # write output_bytes into a file in utf-8