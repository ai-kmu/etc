from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = defaultdict(list)

        # 각 원소를 대각선 그룹으로 분류
        for row_idx, row in enumerate(nums):
            for col_idx, num in enumerate(row):
                diagonal_map[row_idx + col_idx].append(num)
        
        result = []

        # 대각선 순서대로 값을 가져와서 뒤집어 추가
        for key, values in diagonal_map.items():
            result += values[::-1]  # 대각선 순서대로 역순으로 추가

        return result
