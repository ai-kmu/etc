class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        numpath = [0] + [float('inf')] * (amount) # 가장 큰 값으로 amount + 1만큼 배열을 초기화
        
        for coin in coins:
            for value in range(coin, amount + 1):
                # 처음 도착한 위치: numpath[value] = inf, numpath[value - coin] + 1 = inf
                # 처음 도착한 곳이 아닌 위치: numpath[value] = 이전까지 이 위치에 올 수 있었던 최소 동전 개수
                # numpath[value - coin] + 1 = 이번 coin만큼 건너띄기 전의 값에 + 1을 해준 최소 동전 개수 
                numpath[value] = min(numpath[value], 1 + numpath[value - coin])
                
        return numpath[amount] if numpath[amount] != float('inf') else -1 # amount가 inf가 아닌 경우에 최소 동전 개수가 nunpath[amount]에 저장
    
"""
[0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
1 1 inf 1
[0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
2 1 inf 2
[0, 1, 2, inf, inf, inf, inf, inf, inf, inf, inf, inf]  
3 1 inf 3
[0, 1, 2, 3, inf, inf, inf, inf, inf, inf, inf, inf]    
4 1 inf 4
[0, 1, 2, 3, 4, inf, inf, inf, inf, inf, inf, inf]      
5 1 inf 5
[0, 1, 2, 3, 4, 5, inf, inf, inf, inf, inf, inf]        
6 1 inf 6
[0, 1, 2, 3, 4, 5, 6, inf, inf, inf, inf, inf]
7 1 inf 7
[0, 1, 2, 3, 4, 5, 6, 7, inf, inf, inf, inf]
8 1 inf 8
[0, 1, 2, 3, 4, 5, 6, 7, 8, inf, inf, inf]
9 1 inf 9
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, inf, inf]
10 1 inf 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, inf]
11 1 inf 11
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
2 2 2 1
[0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11]
3 2 3 2
[0, 1, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
4 2 4 2
[0, 1, 1, 2, 2, 5, 6, 7, 8, 9, 10, 11]
5 2 5 3
[0, 1, 1, 2, 2, 3, 6, 7, 8, 9, 10, 11]
6 2 6 3
[0, 1, 1, 2, 2, 3, 3, 7, 8, 9, 10, 11]
7 2 7 4
[0, 1, 1, 2, 2, 3, 3, 4, 8, 9, 10, 11]
8 2 8 4
[0, 1, 1, 2, 2, 3, 3, 4, 4, 9, 10, 11]
9 2 9 5
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 10, 11]
10 2 10 5
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 11]
11 2 11 6
[0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6]
5 5 3 1
[0, 1, 1, 2, 2, 1, 3, 4, 4, 5, 5, 6]
6 5 3 2
[0, 1, 1, 2, 2, 1, 2, 4, 4, 5, 5, 6]
7 5 4 2
[0, 1, 1, 2, 2, 1, 2, 2, 4, 5, 5, 6]
8 5 4 3
[0, 1, 1, 2, 2, 1, 2, 2, 3, 5, 5, 6]
9 5 5 3
[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 5, 6]
10 5 5 2
[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 6]
11 5 6 3
[0, 1, 1, 2, 2, 1, 2, 2, 3, 3, 2, 3]
"""
