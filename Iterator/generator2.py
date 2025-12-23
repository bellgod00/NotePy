# generator2.py
import time

def longtime_job():
    print("job start")
    time.sleep(1)  # 1초 지연 - 실제로는 데이터베이스 조회, 파일 처리 등을 시뮬레이션
    return "done"

# 리스트 컴프리헨션: 5번의 작업을 모두 실행해서 리스트로 만든다
#list_job = [longtime_job() for i in range(5)]
#print(list_job[0])  # 첫 번째 결과만 필요한 상황
# 제너레이터 표현식: 함수를 미리 실행하지 않고 필요할 때만 실행  '느긋한 계산법(lazy evaluation)'
list_job = (longtime_job() for i in range(5))
print(next(list_job))  # 1 번째 값만 요청
print(next(list_job))  # 2 번째 값만 요청
print(next(list_job))  # 3 번째 값만 요청
print(next(list_job))  # 4 번째 값만 요청
print(next(list_job))  # 5 번째 값만 요청
print(next(list_job))  # 6 번째 값만 요청