import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# 한글 폰트 지정 (예: NotoSansCJK, 맑은 고딕 등 환경에 따라 변경)
mpl.rcParams['font.family'] = 'Malgun Gothic'  # 윈도우
# 마이너스 기호 깨짐 방지
mpl.rcParams['axes.unicode_minus'] = False

# CSV 읽기: Excel에서 저장한 CSV는 종종 'utf-8-sig' 인코딩이 필요합니다.
df = pd.read_csv(r'D:\01.Project\04.Python\NotePy\numpy\sales.csv', encoding='utf-8-sig', parse_dates=['date'])

# 파생 컬럼: 매출액(amount) = 수량(units) * 단가(price)
df['amount'] = df['units'] * df['price']

# print(" === Sales Data === ")
# print(df.head())
# print("=== DataFrame Info ===")
# print(df.info())

# 일자별 총 매출
daily_sales = df.groupby('date', as_index=True)['amount'].sum()

plt.figure(figsize=(8,4))
daily_sales.plot(marker='o')
plt.title('일별 총 매출 추이')
plt.xlabel('일자')
plt.ylabel('매출액 (원)')
#격자선 설정
# plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
