#Longest Palindromic Substring

#Palindromic Substring : 원래 단어와 그 단어를 거꾸로 해도 똑같은 String
# babab
class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestSubString = ""

        if len(s) <= 1: # 만약 input string의 길이가 1과 같다면
            return s

        #전체 String을 돌면서 substring마다
        #원래 substring과 reversed substring이 같은지 비교
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                print(s[i:j],s[i:j][::-1])
                if len(longestSubString) >= j - i: #만약 현재 substring의 길이가 longestString보다 큰지 확인
                    continue
                elif s[i:j] == s[i:j][::-1]: # 원래 substring과 reversed substring이 같은지 비교
                    longestSubString = s[i:j]

        return longestSubString


if __name__ == '__main__':
    sol=Solution
    input="babad"
    print(sol.longestPalindrome(sol,input))


