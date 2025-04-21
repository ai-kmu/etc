from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Counter로 만들면 각 string에 뭐가 몇 개 있는지 나옴
        s_cnt = Counter(s)
        t_cnt = Counter(t)

        # 1. Counter 특 : 뺄셈 가능
        # 2. `elements` : 어떤 원소가 있는지 iterable 객체로 반환 (`itertools.chain`)
        # 3. 어차피 남은 거 하나니까 `next()`로 끄집어내기
        return next((t_cnt - s_cnt).elements())
