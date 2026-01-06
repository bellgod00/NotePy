
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.family'] = 'Malgun Gothic'
rcParams['axes.unicode_minus'] = False

df = pd.read_csv("TestSample1.csv")

plt.figure(figsize=(7, 4))
plt.scatter(df["quantity"], df["revenue"], c="#9467bd", alpha=0.8, edgecolors="k")
plt.title("수량 vs 매출 산점도")
plt.xlabel("판매 수량")
plt.ylabel("매출(원)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
