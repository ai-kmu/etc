class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1  # row 단위 최소, 최대
        left, right = 0, len(matrix[0]) - 1  # col 단위 최소, 최대

        # row 단위에서 먼저 Binary Search
        while low <= high:
            mid_row = (low + high) // 2
            
            # 이번 row의 최소 최대 사이에 있다면
            if matrix[mid_row][0] <= target <= matrix[mid_row][right]:
                # col 단위에서 Binary Search
                while left <= right:
                    mid_col = (left + right) // 2
                    if matrix[mid_row][mid_col] == target:
                        return True
                    elif matrix[mid_row][mid_col] < target:
                        left = mid_col + 1
                    else:
                        right = mid_col - 1
                
                # 이번 row의 최소 최대 사이에 있어야 되는데 col에서 못 찾으면 없는 거임
                return False
            
            elif matrix[mid_row][0] < target:
                low = mid_row + 1
            else:
                high = mid_row -1
        
        return False
