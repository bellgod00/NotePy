# decorator1.py
import time

def elapsed(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper(*args, **kwargs):   # *args, **kwargs 매개변수 추가
        start = time.time()
        print(f"myfunc()")
        result = original_func(*args, **kwargs)  # 전달받은 *args, **kwargs를 입력파라미터로 기존함수 수행
        end = time.time()
        print(f"함수 수행시간: {end - start} 초")  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 반환한다.
    return wrapper

def elapsed2(original_func):   # 기존 함수를 인수로 받는다.
    def wrapper():
        start = time.time()
        print(f"myfunc()2")
        result = original_func()    # 기존 함수를 수행한다.
        end = time.time()
        print(f"함수 수행시간: {end - start} 초")  # 기존 함수의 수행시간을 출력한다.
        return result  # 기존 함수의 수행 결과를 반환한다.
    return wrapper

@elapsed
def myfunc(msg):
    print("'%s'을 출력합니다." % msg)

@elapsed2
def myfunc2():
    time.sleep(1)
    print("함수가 실행됩니다.")

# decorated_myfunc = elapsed(myfunc)
# decorated_myfunc()
myfunc("You need python")
myfunc2()
