class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        sorted_nums = []

        # extend를 사용후 마지막에 sort로 정렬하여 sorted_nums를 오름차순 숫자의 단일 리스트로서 구현됨
        for i in range(n):
            sorted_nums.extend(matrix[i])
        sorted_nums.sort()

        return sorted_nums[k-1]
