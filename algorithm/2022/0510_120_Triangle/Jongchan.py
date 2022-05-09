'''
시간초과

dfs를 이용해 다음레벨의 자기자신과 같은 인덱스와 그 옆 인덱스 뱡향으로의 탐색
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        answer = float('inf')
        
        def dfs(i, k, sum_of_cur):
            nonlocal answer
            
            if i == len(triangle):
                if sum_of_cur < answer:
                    answer = sum_of_cur
                return
            
            sum_of_cur += triangle[i][k]
            
            dfs(i+1, k, sum_of_cur)
            
            dfs(i+1, k+1, sum_of_cur)
            
        dfs(0, 0, 0)
        return answer
