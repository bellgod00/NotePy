import numpy as np

dim1 = [1, 2, 3] 											# 1차원 데이터
dim2 = [[1, 2, 3, 4], [6, 7, 8, 9]]							# 2차원 데이터
dim3 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]	# 3차원 데이터

# 1차원의 경우 (3, )으로 끊어져있는 모습을 볼 수 있는데, 이는 type이 tuple이라 그런 것이고, 데이터의 개수를 표시해준다.
# 2차원의 경우 (2, 4)로 나누어진 이유는 4개의 데이터가 2묶음 있다는 뜻이다.
# 3차원 데이터의 경우도 마찬가지. (2, 2, 3)로 출력된 이유는 3개의 데이터가 2묶음씩 2개 있다는 뜻이다.

score_numpy = np.array(dim1)
score_numpy.shape
print(score_numpy.shape)

score_numpy = np.array(dim2)
score_numpy.shape
print(score_numpy.shape)

score_numpy = np.array(dim3)
score_numpy.shape
print(score_numpy.shape)

arr = np.array([1.21, 2, 3, 4.4])
print(arr.dtype)
print(arr)

arr = arr.astype('int64')
print(arr)

x = np.array([1, 4, 2, 3, 9])
result = x > 2
print(result)
result.sum()
print(result.sum())
