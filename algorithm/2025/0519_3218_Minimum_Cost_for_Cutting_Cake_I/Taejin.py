import numpy as np
class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Cut cost가 큰 값은 최대한 적게 잘려야함
        # -> Greedy하게 cost 높은 순서대로 cut (1줄씩 잘려나감)
        cost = 0
        horizontalCut.sort()
        verticalCut.sort()

        while horizontalCut and verticalCut:
            if horizontalCut[-1] >= verticalCut[-1]:
                max_cut = horizontalCut.pop()
                cost += (max_cut + sum(verticalCut)) # 1줄 잘리면 경우의 수는 Cut의 sum

            else:
                max_cut = verticalCut.pop()
                cost += (max_cut + sum(horizontalCut)) # 1줄 잘리면 경우의 수는 Cut의 sum

        return cost + sum(horizontalCut) + sum(verticalCut) # 하나라도 크기가 1이면 cut 포함 안되니 나머지 합계까지 계산
