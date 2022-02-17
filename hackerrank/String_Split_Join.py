def split_and_join(line):
    line = line.strip() # 문자열 양쪽에 있는 빈칸 지우기
    result = line.replace(" ", "-") # 문자열들의 빈칸을 '-' 문자로 교체
    return result


if __name__ == '__main__':
    str = input()
    result = split_and_join(str)
    print(result)