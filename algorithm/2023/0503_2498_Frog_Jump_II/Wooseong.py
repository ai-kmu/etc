# cost는 각 점프 중 가장 긴 것에 영향을 받는다.
# 따라서 cost를 최소로 하려면 짧게 점프해야한다.
# 인접한 칸으로 점프하는 것보다 짧을수는 없다.
# 하지만 그러면 돌아올 때 한 칸을 건너뛰어야 해서 길어진다.
# 따라서 항상 한 칸을 건너 뛰도록 만든다.
class Solution:
    def maxJump(self, stones: List[int]) -> int:
        total = len(stones)
        # 예외처리: 길이 == 2이면 하나 밖에 없음
        if total == 2:
            return stones[1] - stones[0]
        else:
            # 숫자가 딱 맞아 떨어지면 1번이 되겠지만, 2번으로 되면 오히려 짧기 때문에 좋음
            # 갈 때: 0 -> 2 -> ... -> 1) -3 -> -1 / 2) -2 -> -1
            go = max(stones[i+2] - stones[i] for i in range(0, total-2))
            # 올 때: -1 -> -3 -> ... -> 1) 3 -> 1 / 2) 2 -> 1
            back = max(stones[i+1] - stones[i] for i in range(1, total-1))

            return max(go, back)
