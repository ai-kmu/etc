class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        max_len = len(sequence) // len(word)
        while word * max_len not in sequence:
            max_len -= 1

        return max_len
