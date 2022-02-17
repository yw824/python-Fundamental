def swap_case(s):
    result = ""
    for ch in s: # s(문자열)를 for문의 대상으로 놓고, ch(문자)를 반복 대상으로 놓을 수 있다.
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result += ch
    return result

# https://blockdmask.tistory.com/416

if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)