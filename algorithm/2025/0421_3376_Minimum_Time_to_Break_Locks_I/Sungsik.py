from bisect import bisect_right

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        # binary search로 탐색하며 풀 수 있는 자물쇠가 생기는 순간 그 중 가장 에너지가 큰 자물쇠를 풀면 될거라 생각
        # 그치만 [7,3,6,18,22,50] 예제에서 해당 방법이 최적이 아닌 것으로 보임
        # 못풀었으니 리뷰 안해주셔도 됩니다
        strength.sort()
        energy = 0
        x = 1
        minute = 0

        while strength:
            minute += 1
            energy += x
            idx = bisect_right(strength, energy)
            if idx > 0:
                energy = 0
                strength.pop(idx-1)
                x += k
        
        return minute
