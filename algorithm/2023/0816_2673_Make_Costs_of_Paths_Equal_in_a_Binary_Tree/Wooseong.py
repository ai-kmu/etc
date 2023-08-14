class Solution:

    def minIncrements(self, n: int, cost: List[int]) -> int:

        ans = 0
        # 역순 탐색: leaf부터 올라오면서 업데이트
        # 같은 parent로부터 나온 두 leaves는 cost가 같아야만 함
        for i in range(n - 1, 1, -2):
            # 두 leaves의 차이만큼 increment 필요
            ans += abs(cost[i - 1]-cost[i])
            # parent (i // 2 - 1)와 leaf를 합쳐서 하나의 노드로 보는 과정
            # 항상 leaf만 보는 것과 같은 효과를 준다
            cost[(i // 2) - 1] += max(cost[i - 1], cost[i])

        return ans
