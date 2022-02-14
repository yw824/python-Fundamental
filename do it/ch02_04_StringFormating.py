# 숫자 바로 대입하기
str = "I eat {0} apples".format(3)
print(str)

# 문자열 바로 대입하기
str = "I eat {0} apples".format("five")
print(str)

# 숫자 값을 가진 변수로 대입하기
number = 3
str = "I eat {0} apples".format(number)
print(str)

# 2개 이상의 값 넣기
number = 10
day = "three"
str = "I eat {0} apples. So I was sick for {1} days".format(number, day)
print(str)

# 이름으로 넣기
str = "I ate {number} apples. So I was sick for {day} days".format(number = 10, day = 3)
print(str)

# 인덱스와 이름을 혼용해서 넣기
str = "I ate {0} apples. So I was sick for {day} days".format(10, day = 3)
print(str)

# 왼쪽 정렬
print("{0:<10}".format("hi"))
# :<10 표현식을 활용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞출 수 있다.

# 오른쪽 정렬
print("{0:>10}".format("hi"))

# 가운데 정렬
print("{0:^10}".format("hi"))

# 공백 채우기
print("{0:=^10}".format("hi"))
# 채워 넣을 문자 값은 정렬 문자인 < , > , ^ 바로 앞에 넣어야 한다.

# 소수점 표현하기
y = 3.42134234
print("{0:0.4f".format(y))
# 소수점 넷째자리까지 표현하는 방법
print("{0:10.4f}".format(y))
# 자릿수를 10으로 맞출 수도 있다.

# { 또는 } 문자 표현하기
print("{{ and }}.".format())
# 중괄호 문자를 포매팅 문자가 아닌 문자 그대로 사용하고 싶다면
# 연속해서 2개를 사용하면 된다.