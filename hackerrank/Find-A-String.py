# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

# string 안에 sub_string 이 몇 개나 있는 지 확인하는 것
# total number of occurrences of the substring in the original string.
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string :
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    print(count_substring(string, sub_string))
    
# 테스트 케이스

#TestCaseTestCase
#CaseT 
#1

#12jlka445kljakldfjlaksjdfdka3942
#3942
#1

#ThIsisCoNfUsInG
#is
#1