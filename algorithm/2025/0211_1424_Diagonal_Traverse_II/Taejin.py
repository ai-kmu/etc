from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        output = defaultdict(list)
        
        # 대각선 탐색에서 같은 대각선 = 행 + 열 값이 같음. 따라서 dict에 대각선별 저장
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                output[i + j].append(nums[i][j])

        ret = []
        # 하나의 리스트로 변환
        for o in output.values():
            ret += o[::-1] # 탐색 시 거꾸로 뒤집어져 reverse

        return ret
