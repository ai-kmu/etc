class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        cnt = len(s) // len(word)
        while True:
            target = word*cnt
            if target in s:
                return cnt
            else: cnt -= 1    
        return 0
