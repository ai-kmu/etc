# 1. x축기준으로 가장 큰거 뽑고 y축 기준으로 가장 큰거 뽑는다
# 2. 뽑힌 2벡터를 가지고 각각 matrix를 만든다
# 3. 두 matrix중 작은 값을 보유하고 있는 애한테서 원본 matrix를 빼준다.
# 4. 다 더한다


# **** 사실 numpy 안쓰는게 더 빠르다 ****

import numpy as np

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)
        x_max, y_max = np.max(grid, axis=1), np.max(grid, axis=0)
        return np.sum(np.minimum(np.repeat([x_max], len(y_max), axis=0),np.repeat([y_max], len(x_max), axis=0).T) - grid)
