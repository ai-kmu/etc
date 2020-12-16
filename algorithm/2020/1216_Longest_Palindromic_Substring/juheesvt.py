"""
brute force

class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = ""
        if len(s) <= 1:
            return s
        
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(long) >= j-i:
                    continue
                elif s[i:j] == s[i:j][::-1]:
                    long = s[i:j]

        return long
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
            
        i,l=0,0
        
        # j로 문자열 s을 순회하면서 s[j-l-1:j+1] -> 즉 j를 기준으로 l+1 만큼의 길이를 가진 substring이 팬린드롬인지 검사하고 i와 l을 업데이트
        for j in range(len(s)):
            # 가장 긴 substring의 시작 idx를 i에 저장하고, 길이는 l에 저장
            if s[j-l: j+1] == s[j-l: j+1][::-1]:
                i, l = j-l, l+1
               
            elif j-l > 0 and s[j-l-1: j+1] == s[j-l-1: j+1][::-1]:
                i, l = j-l-1, l+2
                
        return s[i: i+l]
