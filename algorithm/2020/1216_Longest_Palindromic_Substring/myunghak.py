# DP로 품
# 자기 자신을 포함한 회문을 모두 적어 놓음
# 회문은 다음 방법으로 만듦
# concat (회문의 최소 단위(자기 자신혹은 자기자신과 자기 왼쪽 숫자)  ,  자기하고 한칸 떨어진애의 회문으로 구한 회문)



class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        palin = []
        L,R = 0,1
        for i in range(1,len(s)):
            left_palin = palin
            palin = [1,2] if s[i] == s[i-1] else [1]  # 회문의 최소단위를 넣어줌

            for p in left_palin: # 자기 왼쪽의 회문들을 포함하는 회문을 append해줌
                if (0 <= i-(p+1)) and s[i-(p+1)] == s[i]:
                    palin.append(p+2)
                    
            if palin[-1] > max_length:
                max_length = palin[-1]
                L,R = i-palin[-1] + 1, i+1
        return s[L:R]
