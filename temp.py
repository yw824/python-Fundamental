# 4명의 학생의 이름과 점수를 입력받으세요.
# 학생의 이름은 dictionary의 key로, 학생의 점수는 dictionary의 value로 저장하세요.
students = {"A" : 90,
            "B" : 80,
            "C" : 70,
            "D" : 60}
for i in range(4):
    # 여기를 채우세요!
    print(key)
    if students[i] >= 90:
        print("A")
    elif students[i] >= 80:
        print("B")
    elif students[i] >= 70:
        print("C")
    elif students[i] >= 60:
        print("D")
    else:
        print("F")
    
# 각 학생 별 성적을 "이름: 성적" 형식으로 출력해보세요.
# 점수가 90점 이상이면 A,
# 점수가 80점 이상, 90점 미만이면 B,
# 점수가 70점 이상, 80점 미만이면 C,
# 점수가 60점 이상, 70점 미만이면 D,
# 60점 미만이면 F를 부여합니다.