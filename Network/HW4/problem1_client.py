import requests

def display(r):
    print(r.status_code)
    print(r.headers['Content-Type'])
    print(r.text)

if __name__ == '__main__':
    str = input('Input Keywords>> ')
    s = requests.Session()
    s.headers.update({"Accept-Language": 'en-us, en; q=0.8'})
    r = requests.get("http://localhost:8000/"+str)
    display(r)
