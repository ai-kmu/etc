class Solution:
    def maxJump(self, stones: List[int]) -> int:
        # 돌을 하나 skip하고 뛰어가면서 최대 거리를 찾으면 됨
        n = len(stones)
        if n == 0:
            return 0
        # 돌을 2개만큼 뛰면서 cands에 추가하고 이 중 최댓값을 return
        return max([stones[1] - stones[0]] + [stones[i] - stones[i-2] for i in range(3, n, 2)] + [stones[i] - stones[i-2] for i in range(2, n, 2)])
