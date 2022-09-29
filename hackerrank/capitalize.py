
#str = "hello world my name is lee yong woo"
from pickletools import read_unicodestringnl


#str = '132 456 Wq  m e'
str = '1 2 2 3 4 5 6 7 8  9'
str = 'hello   world  lol'
len = len(str)
ans = ''
mode = 0
for i in range(len):
    if i == 0 or mode == 1:
        if str[i].isalpha():
            ans += str[i].capitalize()
        else:
            ans += str[i]
        mode = 0
        if str[i] == ' ':
            mode = 1
    else:
            ans += str[i]
            if str[i] == ' ':
                mode = 1
print(ans)


# 132 456 Wq  m e
# 1 2 2 3 4 5 6 7 8  9

# ans 
#for x in s[:].split():
#        s = s.replace(x, x.capitalize())
#    return s