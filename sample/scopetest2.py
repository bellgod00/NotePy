# EX1: 함수 안에서 전역 변수 읽기
a = 10 # 전역 변수 (전국구 스타)

def read_global():
    # 함수 안에서도 전역 변수 a에 자유롭게 접근할 수 있습니다.
    print('Ex1 > 함수 내에서 읽기:', a)
read_global()
print('Ex1 > 함수 밖에서 읽기:', a)

# EX2: 이름이 같은 지역 변수와 전역 변수
b = 20 # 전역 변수 b

def shadowing_example():
    b = 30 # 이 b는 함수 안에서만 사는 새로운 '지역 변수'입니다.
    # 이렇게 지역 변수가 전역 변수를 가리는 것을 '섀도잉(shadowing)'이라고 합니다.
    print('Ex2 > 함수 내 지역 변수:', b) # 30
shadowing_example()
print('Ex2 > 함수 밖 전역 변수:', b) # 20 (함수 안의 일은 전역 변수 b에 영향을 주지 못함)

# EX3: 함수 내에서 전역 변수 변경 시도 (⚠️UnboundLocalError 주의)
c = 40 # 전역 변수

def modify_global_fail():
    # 파이썬은 함수 안에서 변수에 값을 할당(=)하면, 그 변수를 무조건 '지역 변수'로 인식합니다.
    # 따라서 아래 코드는 '지역 변수 c에 값을 할당하기 전에 c를 읽으려고 했네?'라고 오해하여 에러를 발생시킵니다.
    # c = c + 10 # UnboundLocalError 발생!
    pass
# modify_global_fail()

# EX4: 'global' 키워드로 전역 변수 수정하기
d = 50 # 전역 변수

def modify_global_success():
    # "지금부터 내가 다루는 d는 지역 변수가 아니라 '전역 변수 d'야!"라고 선언합니다.
    global d 
    d = 60
    print('Ex4 > 함수 내에서 변경된 전역 변수 d:', d)
modify_global_success()
print('Ex4 > 함수 밖에서 변경된 전역 변수 d:', d) # 60 (전역 변수 값이 진짜로 바뀜)

# EX5: 'nonlocal' 키워드 (한 단계 바깥 동네의 변수)
def outer():
    e = 70 # outer 함수의 지역 변수
    print('Ex5 > outer 함수 내 e:', e)
    def inner():
        # "내가 말하는 e는 우리 동네(inner) 것도, 전국구(global)도 아닌,
        # 바로 바깥 동네(outer)의 e야!" 라고 선언합니다.
        nonlocal e 
        e += 10
        print('Ex5 > inner 함수 내 e:', e)
    return inner # inner 함수 자체를 반환

print("여기가 메인인가?...1")
in_test = outer()
print("여기가 메인인가?...2")
in_test() # Ex5 > inner 함수 내 e: 80
print("여기가 메인인가?...3")
in_test() # Ex5 > inner 함수 내 e: 90 (이전 상태를 기억하고 있음)
print("여기가 메인인가?...4")