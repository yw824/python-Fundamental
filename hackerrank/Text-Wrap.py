# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    str = ""
    i = 0
    while i <= len(string):
        if i + max_width > len(string):
            str += string[i:]+"\n"
        else:
            str += string[i:i+max_width] + "\n"
        i = i + max_width
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)