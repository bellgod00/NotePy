lst = [1, 2, 3]

# Iterable: 반복 가능하지만 직접 next()는 안됨
# hasattr() 함수로 확인 : 
print(hasattr(lst, '__iter__'))  # True
print(hasattr(lst, '__next__'))  # False -> 보유하지 않음

## __iter__ : 

# Iterator로 변환
it = iter(lst)

print(f"type(lst): {type(lst)} type(it): {type(it)}")  # <class 'list'>

# Iterator: 반복 가능하고 next()로 값 꺼낼 수 있음
# hasattr() 함수로 확인 : 
print(hasattr(it, '__iter__'))  # True
print(hasattr(it, '__next__'))  # True


print(next(it))  # 1
print(next(it))  # 2