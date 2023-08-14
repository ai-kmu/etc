class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:

        # 완전 이진 트리의 n개의 노드가 주어짐
        # 이진 트리는 1부터 n까지의 숫자
        # 루트는 1이고 각 노드는 2*i의 왼쪽 자식 노드, 2*i + 1의 오른쪽 자식 노드를 갖음
        # cost[i]는 i+1번째 노드의 cost를 의미함.
        # cost의 합이 동일하도록 cost를 더해야하는 데 얼마만큼 더할까

        # cost 라는 list의 값을 갱신해가면서, leaf node부터 위로 쭉 업데이트할 것임

        ans = 0

        for i in range(n // 2 - 1, -1, -1): # 아래 리프노드부터 올라오면서
            l, r = i * 2 + 1, i * 2 + 2 # 왼쪽 노드와 오른쪽 노드에서
            ans += abs(cost[l] - cost[r]) # 맞춰줘야하는 값은 abs로 그냥 구할 수 있음
            cost[i] += max(cost[l], cost[r]) # i번째 cost는 왼쪽과 오른쪽 자식 노드 중 cost가 높은 자식 노드의 값과 더해줌
                                             # 이렇게 했을 때, cost가 max인 path를 기준으로 나머지 노드의 cost가 업데이트 됨
                                             # 이때 ans에 더해주는 cost의 값을 누적해줌으로써, 총 더해지는 cost를 구할 수 있음
        return ans
