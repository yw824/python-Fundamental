def mutate_string(string, position, character):
    temp = list(string) # 리스트로 문자열을 변환
    temp[position] = character # 단순히 해당 인덱스의 글자를 바꾸는 것
    ans = ''.join(temp) # 리스트로 바꿔도 문자열 그대로 join 할 수 있나 보다.
    return ans

if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)