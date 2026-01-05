import numpy as np

# 1D 배열
arr1 = np.array([1, 2, 3, 4, 5])
# 2D 배열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("================================================")
print("1D 배열:", arr1)
print("================================================")
print("2D 배열:\n", arr2)
print("================================================")

# zeros, ones, arange, linspace
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
arange = np.arange(0, 10, 2)  # 0부터 10까지 2 간격
linspace = np.linspace(0, 1, 5)  # 0~1 사이 5개 균등 분할

print("zeros:\n", zeros)
print("================================================")
print("ones:\n", ones)
print("================================================")
print("arange:", arange)
print("================================================")
print("linspace:", linspace)
print("================================================")