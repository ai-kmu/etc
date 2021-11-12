class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Dynamic Programming
        # recursive equation
        # 만약 주변이 모두 자신보다 클 경우 
        # 해당 위치에서 끝나는 path는 오직 자기 자신이므로 1을 저장한다.
        # 만약 주변에 자신보다 작은 숫자가 있을 경우
        # 그 path들 중 가장 긴 것에 +1을 한 것으로 저장한다.
        
        m, n = len(matrix), len(matrix[0])
        # 현재 위치에서 끝나는 path들 중 가장 긴 path의 길이을 저장하는 matrix
        # base case : 자신에서 시작해서 자신으로 끝나는 path (길이=1)
        L = [[1] * n for _ in range(m)]
        
        # 작은 숫자들부터 순회하기 위해 matrix안의 모든 원소를 숫자대로 정렬
        nums = []
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                nums.append((num, i, j))
        nums.sort(key=lambda x: x[0])
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for num, i, j in nums:
            max_length = 1
            for di, dj in directions:
                new_i = i + di
                new_j = j + dj
                if 0 <= new_i < m and 0 <= new_j < n:
                    new_num = matrix[new_i][new_j]
                    # 만약 주변이 자신보다 작을 경우
                    # 해당 주변에서 자신으로 오는 path가 존재함
                    if new_num < num:
                        # 해당 path들 중 가장 긴 것을 고름
                        if L[new_i][new_j] + 1 > max_length:
                            max_length = L[new_i][new_j] + 1
            L[i][j] = max_length
        
        return max(max(x) for x in L)
        
                    
        
