from collections import defaultdict as ddict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = ddict(list)

        # 대각선마다 저장
        for i, row in enumerate(nums):
            for j, val in enumerate(row):
                diag[i + j].append(val)
        
        answer = []
        # 대각선 순서대로 리스트를 병합하는데
        for key in sorted(diag.keys()):
            # 뒤집어야됨
            answer.extend(diag[key][::-1])
        
        return answer
