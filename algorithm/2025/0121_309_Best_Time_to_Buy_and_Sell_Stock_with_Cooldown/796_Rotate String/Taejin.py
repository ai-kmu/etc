class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        flag = False
        idx = 0
        length = len(s)
        while (not flag) and (idx < length):
            if s[idx] == goal[0]:
                flag = ((s[idx:] + s[:idx]) == goal)
                
            idx += 1

        return flag
