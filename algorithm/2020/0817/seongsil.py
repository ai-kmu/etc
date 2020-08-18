class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == "":
            return ""
        for i in range(len(s), 0, -1):  #만들 수 있는 모든 조합을 긴 것부터 차례로 2중 포문으로 구성
            for j in range(len(s) - i + 1):
                if(s[j:j+i] == s[j:j+i][::-1]):  # 뒤집어서 같으면 바로 리턴하고 포문 스탑
                    return s[j:j+i]
