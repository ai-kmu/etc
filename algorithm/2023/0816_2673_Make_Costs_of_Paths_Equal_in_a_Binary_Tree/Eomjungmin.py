class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # 답안 보고 풀었습니다. 그냥 넘기셔도 됩니다. 따로 공부하겠습니다.
        correct = 0
        cost_len = len(cost)
        def dfs(node):
            nonlocal correct
            if node >= cost_len:
                return 0
            lcost=dfs(2*(node+1)-1)
            rcost=dfs(2*(node+1))
            correct+=abs(rcost-lcost)
            return max(lcost,rcost)+cost[node]

        dfs(0)
        return correct
