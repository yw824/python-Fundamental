# 4명의 학생의 이름과 점수를 입력받으세요.
# 학생의 이름은 dictionary의 key로, 학생의 점수는 dictionary의 value로 저장하세요.
students = {"A" : 90,
            "B" : 80,
            "C" : 70,
            "D" : 60}
for key, i in students.items():
    # 여기를 채우세요!
    if students[key] >= 90:
        print("A")
    elif students[key] >= 80:
        print("B")
    elif students[key] >= 70:
        print("C")
    elif students[key] >= 60:
        print("D")
    else:
        print("F")
    
# 각 학생 별 성적을 "이름: 성적" 형식으로 출력해보세요.
# 점수가 90점 이상이면 A,
# 점수가 80점 이상, 90점 미만이면 B,
# 점수가 70점 이상, 80점 미만이면 C,
# 점수가 60점 이상, 70점 미만이면 D,
# 60점 미만이면 F를 부여합니다.

import random

alist = []  # 뽑은 a를 넣어 중복 방지해주는 리스트
for i in range(30):
    a = random.randint(1, 30)
    alist.append(a)  # 새로운 a 값을 리스트에 추가

print(alist)
