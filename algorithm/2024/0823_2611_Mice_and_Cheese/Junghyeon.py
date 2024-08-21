# 풀이 실패....
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        reward1.sort()
        reward2.sort()

        return sum(reward1[-k:]) + sum(reward2[-k:])
