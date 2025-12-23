# Numpy 사용
import time
import numpy as np

# start = time.time()
# arr = [i for i in range(100000000)]
# end = time.time()
# print('list 1억개 생성 소요시간은 ', end-start, '초입니다.')

start = time.time()
arr = np.arange(100000000)
end = time.time()
print('numpy array 1억개 생성 소요시간은 ', end-start, '초입니다.')
