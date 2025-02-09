class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = [[] for _ in range(m+n-1)]

        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                # 같은 대각선의 num은 i + j가 같음을 이용
                diagonals[i+j].append(num)
        
        # 역순으로 집어넣었기 때문에 diagonal을 reverse
        return [num for diagonal in diagonals for num in reversed(diagonal)]
