from bisect import bisect_left

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        m = len(matrix)
        n = len(matrix[0])
        # 정렬한 숫자를 넣어줄 빈 array 생성
        nums = []

        # matrix 안의 모든 값을 확인
        for i in range(m):
            for j in range(n):
                num = matrix[i][j]
                # 해당 값이 num의 어느 위치에 들어갈 지 바이너리로 찾아 줌
                idx = bisect_left(nums, num)
                # 해당 인덱스에 넣어줌 
                nums.insert(idx, num)
        
        # 인덱스가 0부터 시작이기 때문에 k-1 번째 값 리턴         
        return nums[k-1]
