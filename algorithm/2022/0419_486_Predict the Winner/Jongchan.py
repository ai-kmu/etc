# dfs를 이용한 재귀로 풀어보려고 했으나, 계속 오답이 나와 Solution을 참고해 풀었습니다.
'''
    전체의 과정을 보며 player1과 player2가 모두 유리한 방향으로 숫자를 뽑는다.
    따라서 dfs를 따라 가장 마지막 카드까지 뽑았을 때부터,
    경우의 수를 역으로 따지기 시작해 서로에게 유리한 방향으로 값을 가져온다.
    
    ex) [1, 5, 233, 7]
    
    p1           1                 7
    p2       5       7        1        233
    p1    233  7   5  233   5  233    1   5
    p2     7  233 233  5   233  5     5   1
    
    3번째 층에서 p1이 유리하려면 각각 233, 233, 233, 5를 택해야함.
    2번째 층에서 p2가 유리하려면, 마지막 층에서 p1이 선택한 값과 비교해서
    둘중어 어떤 것을 선택하는 것이 그나마 더 유리한지 선택함.
    -> 각각 7, 233 쪽을 선택.
    맨 위층에서 1을 선택 했을때가 p1이 233을 가지고 있으므로 최대가 됨.
    따라서 1을 선택하고 p1이 이기게 됨.
'''

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def dfs(s, e, turn=1): # player1부터 시작
            
            if s == e: # 마지막 턴의 경우
                return turn * nums[s]
            
            # turn을 곱하므로써 player1과 2의 차례구별
            # turn이 1일때가 player1의 차례
            # turn을 이용해 player1의 점수에서 player2의 점수를
            # 빼므로써 둘 중 누가 더 높은 점수를 가지고 있는지 알 수 있음
            a = turn * nums[s] + dfs(s + 1, e, -turn)
            b = turn * nums[e] + dfs(s, e - 1, -turn)
            
            # player1은 큰 값을, player2는 작은 값을 반환
            if turn == 1:
                return max(a, b)
            else:
                return min(a, b)
        
        
        return dfs(0,len(nums)-1) >= 0
