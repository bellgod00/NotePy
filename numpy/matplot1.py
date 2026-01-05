
import matplotlib.pyplot as plt
from matplotlib import rc # runtime configuration for matplotlib 설정함수


# 폰트 패밀리 설정 (예: 맥은 'AppleGothic', 윈도우는 'Malgun Gothic', 리눅스는 'NanumGothic' 등)
rc('font', family='Malgun Gothic')   # 환경에 맞는 폰트로 변경하세요.
rc('axes', unicode_minus=False)      # 마이너스 기호가 □ 로 깨지는 현상 방지

# 간단한 라인 플롯 그리기
plt.plot([1, 2, 3], [10, 20, 15])
plt.title("간단한 라인 플롯")
plt.show()
