class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length = 0
        n = len(t)
        
        for c in s:
            # 문자가 같을 경우 length를 1 증가
            if c == t[length]:
                length += 1
            if length >= n:
                break
                
        
        return n - length
        
