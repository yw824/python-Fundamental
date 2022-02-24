# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

ans = [False, False, False, False, False]

def Validator(str):
    if str.isalnum(): ans[0] = True
    if str.isalpha(): ans[1] = True
    if str.isdigit(): ans[2] = True
    if str.islower(): ans[3] = True
    if str.isupper(): ans[4] = True


# 기본 입력 상태
if __name__ == '__main__':
    s = input()
    num = len(s)

    for i in s:
        Validator(i)
    for i in ans:
        print(i)

