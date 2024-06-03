class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        for char in s:
            if char == t[t_index]:
                t_index += 1
                if t_index == len(t):
                    break
        return len(t) - t_index
