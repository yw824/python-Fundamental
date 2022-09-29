import string
import random

remain_alp = list(string.ascii_uppercase)  # 남은 알파벳
print(remain_alp)

if 'A' in remain_alp:
    print("A exists")
else:
    print("A never exists")

remain_alp.remove('A')
print(remain_alp)

if 'A' in remain_alp:
    print("A exists")
else:
    print("A never exists")