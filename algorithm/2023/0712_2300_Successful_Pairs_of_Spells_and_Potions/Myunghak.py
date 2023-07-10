# 문제를 다르게 생각하면 각 potion 중 success / spells 이상의 것이 몇개나 있는지임
# 위 문제를 풀기 위해 우선 potion을 정렬시킴
# bisect_right로 success / spells의 값을 찾음
# 현재 potion을은 정렬되어 있으므로 그것보다 큰것들의 개수가 답

class Solution:
    def successfulPairs(self, spells, potions, success):
        ans = []
        potions.sort()
        for p in spells:
            idx = bisect_right(potions, success / p - 0.0000001)
            ans.append(len(potions) - idx)
        return ans
