from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        remain = lambda x: any([y > 0 for y in x.values()])
        n = len(s)

        l, r = 0, 0
        answer = False
        while l < n and r < n:
            while remain(counter) and r < n:
                if s[r] in counter:
                    counter[s[r]] -= 1
                r += 1
            if remain(counter):
                break
            while not remain(counter) and l < n:
                if s[l] in counter:
                    counter[s[l]] += 1
                l += 1
            if not answer or r - l + 1 < len(answer):
                answer = s[l-1:r]
        
        return answer if answer else ""
