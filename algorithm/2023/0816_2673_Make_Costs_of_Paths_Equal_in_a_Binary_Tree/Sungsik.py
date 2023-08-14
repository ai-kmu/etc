class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # 현재 노드에서 아래 두 subtree는 위 조건을 만족한다고 하면
        # 두 subtree들 중 cost를 높은 것을 골라 작은 subtree cost와의 차이만큼 root에 더해주면 된다.
        answer = 0
        
        def dfs(i):
            # leaf node이면 그대로 출력
            if i >= n // 2:
                return cost[i]
            
            nonlocal answer
            # 왼쪽, 오른쪽 subtree의 cost를 가져옴
            left, right = dfs(2 * i + 1), dfs(2 * i + 2)
            
            # 차이만큼 더함
            # 둘 중 작은 subtree의 root에 answer만큼 더해야 하지만
            # 어차피 cost만 중요한 것이므로 그렇게 하진 않는다
            answer += abs(left - right)
            
            return cost[i] + max(left, right)
    
        dfs(0)
        return answer
            
                
