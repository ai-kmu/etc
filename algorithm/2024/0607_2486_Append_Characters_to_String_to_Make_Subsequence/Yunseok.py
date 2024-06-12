class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        target_index = 0
        target_length = len(t)

        for char in s:
            if target_index < target_length and char == t[target_index]:
                target_index += 1
        
        return target_length - target_index
