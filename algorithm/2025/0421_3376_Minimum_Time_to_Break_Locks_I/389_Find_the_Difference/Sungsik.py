from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s, counter_t = Counter(s), Counter(t)

        for k, v in counter_s.items():
            if v != counter_t[k]:
                return k
            else:
                counter_t.pop(k)
        return list(counter_t.keys())[0]
