# This is a sample Python file to demonstrate a range test.

print("Testing range function:")
for i in range(10):
    print(i)

print("Testing range with start and end:")
for i in list(range(5, 10)):
    print(i)  

print("Testing range with step:")
for i in list(range(0, 10, 3)):
    print(i)  

print("Testing range with negative step:")
for i in list(range(-10, -100, -30)):
    print(i)  

print("Testing range with len of a list:")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])