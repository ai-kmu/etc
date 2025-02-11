class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if word not in sequence:
            return 0
        
        sequence_len = len(sequence)
        word_len = len(word)
        left = 1
        right = sequence_len // word_len

        while left <= right:
            middle = (left + right) // 2
            if word * middle in sequence:
                left = middle + 1
            else:
                right = middle - 1 
                
        return left - 1
