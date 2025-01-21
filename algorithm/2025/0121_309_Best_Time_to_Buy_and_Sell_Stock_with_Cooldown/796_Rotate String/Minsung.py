class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s == goal:
                return True
            s = self.rotate_str(s)
        return False
    
    def rotate_str(self, s: str):
        s = s[1:] + s[0]
        return s
