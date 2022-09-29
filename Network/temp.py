str = b'123?'
temp = str.decode()
print(temp)
temp2 = temp[:-2]
print(temp2)
ans = int(temp2)
print(ans)