import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])# 1D 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])# 2D 배열

# 배열의 각 차원 크기(튜플)
print(arr1.shape)   # (5,)
print(arr2.shape)   # (2, 3)
# 차원(축) 수
print(arr2.ndim)    # 2
# 전체 원소 개수 (np.prod(a.shape)와 동일)
print(arr2.size)    # 6
#dtype: 데이터 타입 (읽기/쓰기 가능)
#itemsize: 한 원소의 바이트 수 (dtype에 의해 결정)
#nbytes: 전체 배열의 바이트 수 (size * itemsize)
#strides: 메모리에서 다음 요소까지 건너뛸 바이트 수(차원별)




# zeros, ones, arange, linspace
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
arange = np.arange(0, 10, 2)  # 0부터 10까지 2 간격
linspace = np.linspace(0, 1, 5)  # 0~1 사이 5개 균등 분할

# dtype 확인 및 변경
print(zeros.dtype)              # float64
zeros_int = zeros.astype(int)   # 정수형으로 변환

# 슬라이싱/인덱싱
print(arr2[0, :])   # 첫 번째 행 -> [1 2 3]
print(arr2[:, 1])   # 두 번째 열 -> [2 5]

# 브로드캐스팅 예시
print(arr2 + 10)    # 모든 원소에 10 더하기
print(arr2 * np.array([1, 2, 3]))  # 각 열에 다른 계수 곱하기 (브로드캐스팅)

# reshape
print(np.arange(12).reshape(3, 4))

