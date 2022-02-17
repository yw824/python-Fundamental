def print_full_name(first, last):
   str = "Hello "
   str += first 
   str += ( " " + last )
   str += "! You just delved into python."
   print(str)
# 딱히 건들거 없음, 단위마다 문자열 뒤에 추가해주면 됨

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)