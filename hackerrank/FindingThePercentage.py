if __name__ == '__main__':
    n = int(input())
    student_marks = {} # 딕셔너리 : key를 이름으로, value를 리스트로 설정
    for _ in range(n):
        name, *line = input().split()
        # *는 가변수를 의미
        # https://hcnoh.github.io/2019-01-27-python-arguments-asterisk
        # print(line)
        scores = list(map(float, line))
        # 첫 번째 인자에 자료형, 두 번째 인자에 리스트 넣어서 해당 형으로 리스트 만들기
        # https://dojang.io/mod/page/view.php?id=2286
        student_marks[name] = scores
    query_name = input()
    temp = sum(student_marks[query_name])
    print(format(temp/3, ".2f"))

# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
# main 으로 변경 후 전송 2번째
