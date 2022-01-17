# 발표자 comment
# 굳이 edge라는 변수를 만들어 나중에 result에 붙여주는 이유가 있나요?
# 마지막 elif문은 else로 대체하는 것이 속도면에서는 이득입니다.

import numpy as np


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # slice해야 하는 edge의 위치를 나타내는 변수
        # 0: 위쪽, 1: 오른쪽, 2: 아래쪽, 3: 왼쪽
        direction = 0
        # column의 slicing을 위해 numpy를 사용
        np_matrix = np.array(matrix)
        result = []
        
        while np_matrix.size != 0:
            # 위쪽 edge
            if direction == 0:
                edge = list(np_matrix[0,:])
                np_matrix = np_matrix[1:,:]
            
            # 오른쪽 edge
            elif direction == 1:
                edge = list(np_matrix[:,-1])
                np_matrix = np_matrix[:,:-1]
            
            # 아래쪽 edge => 순서를 반대로 저장해야 하기 때문에 np.flip을 사용
            elif direction == 2:
                edge = list(np.flip(np_matrix[-1,:]))
                np_matrix = np_matrix[:-1,:]
            
            # 왼쪽 edge => 순서를 반대로 저장해야 하기 때문에 np.flip을 사용
            elif direction == 3:
                edge = list(np.flip(np_matrix[:,0]))
                np_matrix = np_matrix[:,1:]
            
            direction = (direction + 1) % 4
            result += edge
        
        return result
