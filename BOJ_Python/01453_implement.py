List = [0]*101

n = int(input())
m = -1
cnt = 0
lst = map(int, input().split())
for i in lst:
    if List[i] == 0:
        List[i] = 1
    else:
        cnt += 1

print(cnt)
