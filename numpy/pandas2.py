
import pandas as pd

# CSV 파일 읽기 (첫 행을 헤더로 사용)
df = pd.read_csv("TestSample1.csv")  # 예: 컬럼은 date, product, region, quantity, revenue

# 상위 5행 확인
print(df.head())

# 컬럼/결측치/타입 등 요약
print(df.info())

# 수치 컬럼의 기술통계
print(df.describe())
