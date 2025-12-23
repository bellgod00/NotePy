a = "Life is too short"
b = a.encode('utf-8')
c = a.encode("ascii")

print(a)  # Life is too short
print(b)  # b'Life is too short'
print(c)  # b'Life is too short'

print(f"type(a): {type(a)} type(b): {type(b)} type(c): {type(c)}")

a = "한글"
b = a.encode('euc-kr')
c = a.encode('utf-8')

print("\n\n")  # 한글

print(a)  # 한글
print(b)  # b'\xc7\xd1\xb1\xdb'
print(c)  # b'\xed\x95\x9c\xea\xb8\x80' 

print(f"type(a): {type(a)} type(b): {type(b)} type(c): {type(c)}")


