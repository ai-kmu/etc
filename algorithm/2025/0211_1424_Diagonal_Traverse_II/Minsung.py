from collections import deque, defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag = defaultdict(deque)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diag[i+j].appendleft(nums[i][j])  # 각 diagonal 요소의 좌측부터 저장

        ans = list()
        for k, v in diag.items():  # 각 diagonal 요소 concat
            ans += list(v)
        return ans
