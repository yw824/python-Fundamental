import whois

# 교재에서는 아래의 방식으로 값을 얻었다.
whois.whois('ssu.ac.kr')

domain_info = whois.whois('ssu.ac.kr')
print(domain_info)
