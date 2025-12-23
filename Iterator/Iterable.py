#  Iterable : 객체는 반복할 수 있는 객체 
#  Iterator : 반복자, 반복할 수 있는 객체에서 값을 하나씩 꺼내오는 역할
#  Iterable vs Iterator
#  Iterable : __iter__() 메서드를 가지고 있는 객체
#  Iterator : __iter__() 메서드와 __next__() 메서드를 모두 가지고 있는 객체
#  Iterable 객체는 iter() 함수를 사용하여 Iterator 객체로 변환할 수 있습니다
#  Iterator 객체는 next() 함수를 사용하여 다음 값을 얻을 수 있습니다
#  Iterator 객체에서 더 이상 꺼낼 값이 없으면 StopIteration 예외를 발생시킵니다   
l = [1, 2, 3]
t = (3, 4)
d = {'a': 1, 'b': 2}
s = set()
r = range(10)

print(iter(l))
print(iter(t))
print(iter(d))
print(iter(s))
print(iter(r))

## iter : 반복 가능한 객체를 반복자 객체로 변환 

iterator = iter([1, 2, 3, 4, 5])

print(next(iterator))
print(next(iterator))
print(next(iterator))

print(f"여기서 부터 for문이다.")

for n in iterator:
    print(n)

