import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# 1. 한글 폰트 설정 (윈도우: Malgun Gothic, 맥: AppleGothic)
rc('font', family='Malgun Gothic')

# 2. 가상의 데이터 생성 (월별 커피 지출액)
data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월'],
    '지출(원)': [35000, 32000, 45000, 80000, 40000, 38000]
}

# 3. Pandas DataFrame으로 변환
df = pd.DataFrame(data)
# print(df[df['지출(원)'] >= 40000])  # 조건에 맞는 행

#결과 데이터 프레임 형식으로 보면 보기 편한 표로 나옵니다
# 4. 데이터 확인 일반 출력으로 출력시
# print("=== 내 커피 지출 데이터 ===")
# print(df)

# 5. 그래프 그리기 (막대 그래프)
plt.figure(figsize=(10, 6)) # 그래프 크기 설정
plt.bar(df['월'], df['지출(원)'], color='skyblue') # 막대 그래프 생성

plt.title('상반기 월별 커피 지출 내역') # 제목
plt.xlabel('월') # x축 이름
plt.ylabel('금액(원)') # y축 이름

plt.show() # 그래프 출력






