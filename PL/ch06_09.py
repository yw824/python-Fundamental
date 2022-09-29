x = 1
y = 3
z = 5

def sub1() : 
    print("-------------sub1-------------------")
    a = 7
    y = 9
    z = 11
    print("a:",a)
    print("x:",x)
    print("y:",y)
    print("z:",z)

def sub2():
    print("-------------sub2-------------------")
    global x
    a = 13
    x = 15
    w = 17

    print("a:",a)
    print("x:",x)
    print("y:",y)
    print("z:",z)
    print("w:",w)


    def sub3():
        print("-------------sub3-------------------")
        nonlocal a
        a = 19
        b = 21
        z = 23


sub1()

print("-------------main-------------------")
print(x)
print(y)
print(z)

sub2()

print("-------------main-------------------")
print(x)
print(y)
print(z)

sub3()
