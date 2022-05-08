from collections import deque


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 위에서부터가 아닌 아래서부터 시작
        # dp의 값은 각 노드가 루트인 sub-triangle에서의 minimum path sum
        dp = [[-1] * len(row) for row in triangle]
        
        # base case: leaf node는 자기 자신
        for i in range(len(triangle[-1])):
            dp[-1][i] = triangle[-1][i]
            
        for i in range(len(triangle)-2, -1, -1):
            for k in range(i+1):
                # 왼쪽 sub-triangle과 오른쪽 sub-triangle의 최솟값과 현재 위치의 값을 더함
                dp[i][k] = min(dp[i+1][k], dp[i+1][k+1]) + triangle[i][k]
        
        return dp[0][0]
