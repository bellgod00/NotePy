# generator1.py
def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result
# yield 키워드가 있으면 함수는 제너레이터가 된다.
# yield : 값을 하나씩 반환하면서 함수의 상태를 기억

gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))