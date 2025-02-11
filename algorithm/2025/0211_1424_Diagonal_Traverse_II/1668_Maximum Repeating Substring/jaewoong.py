class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        repeated_word = word
        while repeated_word in sequence:
            k += 1
            repeated_word = word * (k + 1)
        return k        
