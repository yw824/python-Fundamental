import random
import math
import time

n = 0
num = []
prime = []

def setPrime(max):
    for i in range(2, int(math.sqrt(max))):
        if prime[i] == False:
            continue
        j = 2

        while( i * j ) <= max:
            prime[ i * j ] = False
            j += 1

def getPrime(Start, End):
    ans = 0
    for i in range(Start, End + 1):
        if prime[i]:
            ans += 1
    return ans


if __name__ == "__main__":

    startTime = time.time()

    n = int(input(">> Input the number of numbers to process: "))
    num = random.sample(range(100000), n)

    #n = 11
    #num = [368, 12, 58, 74, 712, 12, 38, 1110, 1612, 4, 222]

    num.sort()
    
    # get GCD
    _gcd = num[0]
    for i in num[1:]:
        _gcd = math.gcd(_gcd, i)
    print(">> Input the numbers to be processed:")
    print(num)
    print("GCD of input numbers is : {}".format(_gcd))

    # Set Prime Numbers
    max = num[n-1]
    #print("max : {}".format(max))

    prime = [True] * ( max + 1 )
    prime[0] = False
    prime[1] = False
    
    setPrime(max)
    
    # get Prime Numbers between arr[ i ] & arr[ i + 1 ]
    for i in range(1, n):
        if num[i-1] != num[i]:
            print("Number of Prime Numbers Between {} , {} : {}".format(num[i-1], num[i], getPrime(num[i-1], num[i])))

    print( "Total execution time using Python is {} seconds!".format(time.time()-startTime) )
