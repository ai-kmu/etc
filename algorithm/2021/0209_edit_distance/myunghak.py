# Edit distance의 dist_mat을 사용

import numpy as np
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        
        # dist_mat의 기본 틀 생성
        dist_mat = np.zeros((l1+1,l2+1), dtype = int)
        dist_mat[0] += np.linspace(0,l2,l2+1, dtype = int)
        dist_mat[:,0] += np.linspace(0,l1,l1+1, dtype = int)
        
        # 만약 선택된 두 문자가 같으면 왼쪽위에서 그대로 가져오고 다르면 위, 왼쪽위, 왼쪽 중 가장 작은것에 1을 더해 가져온다
        for i in range(l1):
            for j in range(l2):
                if word1[i] != word2[j]:
                    dist_mat[i+1,j+1] = min(dist_mat[i,j+1], dist_mat[i+1,j], dist_mat[i,j]) + 1
                else:
                    dist_mat[i+1,j+1] = dist_mat[i,j]
            
        return dist_mat[-1][-1]
        
