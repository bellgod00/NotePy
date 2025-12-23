import numpy as np

arr1 = np.array([[1, 2, 3, 4],[11, 12, 13, 14]])
arr2 = np.array([[5, 6, 7, 8],[15, 16, 17, 18]])

# 위 두가지 기능 모두 데이터를 행으로 합쳐준다.
# concatenate(axis=0)
np.concatenate((arr1, arr2), axis=0)
# vstack
np.vstack((arr1, arr2))
print("=== axis=0 ===")
print(np.concatenate((arr1, arr2), axis=0))
print(" === vstack ===")
print(np.vstack((arr1, arr2)))  

# 위 두가지 기능 모두 데이터를 열으로 합쳐준다.
# concatenate(axis=1)
np.concatenate((arr1, arr2), axis=1)
# hstack
np.hstack((arr1, arr2))
print("=== axis=1 ===")
print(np.concatenate((arr1, arr2), axis=1))
print(" === hstack ===")
print(np.hstack((arr1, arr2)))  