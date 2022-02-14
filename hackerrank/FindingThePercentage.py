if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    temp = sum(student_marks[query_name])
    print(format(temp/3, ".2f"))

# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
