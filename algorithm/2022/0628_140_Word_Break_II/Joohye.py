#오답

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        # 중복되지않은 단어 word_set에 저장
        word_set = set(wordDict)
        # dp 정의
        dp = {0: ['']}
        
        # 재귀 풀이
        def recursive(i):            
            if i in dp:
                return dp[i]
            dp[i] = []
            j = i - 1
            while j >= 0:
                # 슬라이싱 한 값이 word_set에 있으면
                if s[j:i] in word_set and recursive(j) != []:
                    for s_break in dp[j]:
                        dp[i].append(s_break + (' ')+ s[j:i])
                j -= 1
            return dp[i]
        return recursive(len(s))
        
