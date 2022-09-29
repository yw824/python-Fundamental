def special_bits(L=1, R=10, k=1):
    num=-1

    for i in range(L, R+1):
        count = 0
        stand = 1
        while stand <= i:
            if i & stand != 0:
                count += 1
            stand *= 2

        if count == k:
            if num == -1:
                num = i
                break
        
    return num


if __name__ == "__main__":
    print('\n\n' + '.'*20 + 'Problem 1' + '.'*20)
    if special_bits(1, 10, 1) != 1:
        print("incorrect!")
    if special_bits(L=1, R=10, k=2) != 3:
        print("incorrect!")
    if special_bits(L=1, R=10, k=3) != 7:
        print("incorrect!")
    if special_bits(L=1, R=10, k=4) != -1:
        print("incorrect!")