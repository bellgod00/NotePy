
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False

df = pd.read_csv("TestSample1.csv", parse_dates=["date"])

# 날짜×상품 피벗 (매출 합계)
pivot = df.pivot_table(index="date", columns="product", values="revenue", aggfunc="sum")

# 결측치 0 처리(시각화용)
pivot = pivot.fillna(0)

pivot.plot(kind="bar", figsize=(10, 4))
plt.title("일자×상품 매출(그룹 막대)")
plt.xlabel("일자")
plt.ylabel("매출(원)")
plt.legend(title="상품", bbox_to_anchor=(1.02, 1), loc="upper left")
plt.tight_layout()
plt.show()
