def func(str): 
    ans = ''
    for s in str:
        if(s.lower() == s):
            ans += s.upper()
        else:
            ans += s.lower()
    print(ans)

if __name__ == "__maina__":
    str1 = "ANkit"
    str2 = "abCDe"

    func(str1)
    func(str2)
