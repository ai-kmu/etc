class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        happy = "dd" # dummy
        candidates = [["a", a], ["b", b], ["c", c]]
        candidates.sort(key=lambda x:x[1] - (100 if happy[-1]==happy[-2]==x[0] else 0)) # 이전에 두번 나타났으면 패널티로 우선순위 미룸

        while candidates[-1][1] > 0:
            happy += candidates[-1][0] # happy 추가
            candidates[-1][1] -= 1 # candidates 값 감소
            candidates.sort(key=lambda x:x[1] - (100 if happy[-1]==happy[-2]==x[0] else 0)) # 이전에 두번 나타났으면 패널티로 우선순위 미룸

        return happy[2:]
