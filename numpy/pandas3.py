
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rcParams

# 한국어 폰트 설정 (윈도우: Malgun Gothic, 맥: AppleGothic, 리눅스/범용: NanumGothic 등)
# 설치된 폰트 중 사용 가능한 것으로 설정하세요.
rcParams['font.family'] = 'Malgun Gothic'  # 필요 시 'AppleGothic' 또는 'NanumGothic'
rcParams['axes.unicode_minus'] = False     # 음수 표시 깨짐 방지

df = pd.read_csv("TestSample1.csv", parse_dates=["date"])

# 진단: 컬럼/타입/샘플 확인
print("columns:", df.columns.tolist())
print(df.head())
print(df.info())
print("date dtype:", df["date"].dtype)
print("revenue dtype (before):", df["revenue"].dtype)

# 수치형 강제 변환 및 결측 확인
# (문자열 형식의 숫자가 있다면 NaN으로 바뀔 수 있음)
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
print("revenue NaNs after coercion:", df["revenue"].isna().sum())

# 일자별 총매출
daily_rev = df.groupby("date", as_index=True)["revenue"].sum().sort_index()

plt.figure(figsize=(9, 4))
plt.plot(daily_rev.index, daily_rev.values, marker="o", color="#1f77b4")
plt.title("일자별 총 매출 추이")
plt.xlabel("일자")
plt.ylabel("매출(원)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
