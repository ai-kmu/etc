""" 
삼각형의 위에서 아래로 이동하는데 인접한 숫자로 이동하면서 워소의 최소 합을 찾는 문제
ex. [[2], [3,4], [6,5,7], [4,1,8,3]] => (2 + 3+ 5+ 1) = 11

      2
     3 4
    6 5 7
   4 1 8 3        <--여기서 출발
  
bottom up 방식으로 풀 수 있다.
인접한 두 요소에서 [i+1][j] vs [i+1][j+1]의 최소값을 찾는다.
그런다음 그때의 요소값을 추가하고 싶다. 
그래서 이렇게 재귀적으로 표현할 수 있다.
triangle[i] + min( dp[j], dp[j+1] ) + triangle[i][j]
bottom up 방식으로 맨 아래행부터 보면서 돌겠다.
"""

class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle) # 삼각형의 총 층 수

        dp = triangle[n-1] # dp를 삼각형의 마지막 레이어로 시작, n-1이어야 마지막층 인덱스가 됨
        print(n)
        for i in range(n-2,-1,-1): # 마지막 층에서 위로 한칸씩 이동하면서
            for j in range(i+1): # 층에서의 각 요소를 돌면서
                dp[j] = min( dp[j], dp[j+1] ) + triangle[i][j] # 최소를 찾아 현재 원소를 더해서 dp 변경

        return dp[0] # 밑에서부터 0번째 층까지의 최소합 return
