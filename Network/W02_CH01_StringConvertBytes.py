# 강의교안 Introduction to Client-Server Networking (Part 2) - 11페이지
# Preliminaries : Encoding and Decoding

print("generate 10 zero bytes")
print(bytes(10)) #generate 10 zero bytes

print("generate 5 bytes")
print(bytes([10, 20, 30, 40, 50])) # generate 5 bytes

print("generate text as byte data type")
a = b'hello' # generate text as byte data type
print(a)
# b'' indicates byte data type for string inside '' or ""
print("typeof b'[string]'")
print(type(a))
print("convert bytes to String")
b =str(a)
print(type(b))