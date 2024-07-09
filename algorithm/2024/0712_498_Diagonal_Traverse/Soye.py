from collections import deque
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 각 대각선 요소를 저장할 딕셔너리 생성
        cac, ROWS, COLS = {}, len(mat), len(mat[0])
        
        # 행렬의 각 요소를 순회
        for i in range(ROWS):
            for j in range(COLS):
                k = i + j  # 현재 대각선을 나타내는 키
                
                # 대각선 키가 딕셔너리에 없으면 빈 덱(deque)을 추가
                if k not in cac:
                    cac[k] = deque()
                
                # 대각선 키가 홀수면 오른쪽에 요소 추가, 짝수면 왼쪽에 요소 추가
                if k % 2 == 1:
                    cac[k].append(mat[i][j])
                else:
                    cac[k].appendleft(mat[i][j])
        
        # 딕셔너리에 저장된 덱(deque)을 평탄화하여 단일 리스트로 반환
        return [k for _, j in cac.items() for k in list(j)]
