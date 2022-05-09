'''
- 그냥 dfs 쓰면 Time Limit Exceeded가 발생..
- 그래서 memoization 기법을 사용해서 반복 연산을 줄여주는 방식으로 문제 해결
- key 값은 index 쌍(row, column)에 해당하고, value는 minimum path sum
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def dfs(triangle, d, idx, memo={}):
            
            # 만약 d(depth)가 len(triangle)과 동일하다면, 제일 밑의 row 까지 탐색한거니까 종료
            if d == (len(triangle) -1):
                return triangle[d][idx]
            
            # (d, idx) 조합이 memo에 저장되어 있지 않은 경우에만 (--> 반복연산을 줄여주기 위해서)
            # 현재 지점에서 하나 밑의 row(d+1)에서 idx, idx+1 중에 더 작은 값을 현재 위치(triangle[d][idx]) 와 더해줌
            if (d, idx) not in memo:
                memo[(d, idx)] = triangle[d][idx] + min(dfs(triangle, d+1, idx), dfs(triangle, d+1, idx+1))
                
            return memo[(d, idx)]
        
        return dfs(triangle, 0, 0)
            
            
