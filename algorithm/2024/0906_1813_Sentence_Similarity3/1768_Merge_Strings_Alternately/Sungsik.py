class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        remain = word1[n:] if len(word1) > len(word2) else word2[n:]
        return ''.join([f'{x}{y}' for x, y in zip(word1[:n], word2[:n])]) + remain
