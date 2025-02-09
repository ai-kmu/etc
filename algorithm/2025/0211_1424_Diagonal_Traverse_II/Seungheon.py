class Solution(object):
    def findDiagonalOrder(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """

        # 0,0 0,1 0,2
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2

        # (row_idx, col_idx, value)
        row_col_value_list = [(r, c, nums[r][c]) for r in range(len(nums)) for c in range(len(nums[r]))]
        
        # 정렬 : (row_idx + col_idx), col_idx, row_idx 순
        row_col_value_list.sort(key=lambda x: (x[0] + x[1], x[1], x[0]))

        return [val for _, _, val in row_col_value_list]
