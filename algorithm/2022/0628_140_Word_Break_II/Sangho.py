from typing import List

# dfs 문제
# recursion func 사용해서 문제풀이

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def recursion(s, i, new_str) :
            if i == len(s) :  # s에 남은 문자가 없으면 : ans에 append하고 끝
                ans.append(" ".join(new_str))
                return ans  
            elif i < len(s) : # s에 남은 문자가 있으면 : wordDict에 있는 단어로 check
                for word in wordDict :
                    j = len(word) # wordDict에서 word하나 뽑고 길이 j로 저장
                    
                    if s[i : i+j] == word : # s[i : i+j] 가 뽑은 word랑 같은지 check
                        recursion(s, i+j, new_str + [word])  # 조건 만족하면 :  new_str에 word 추가하고, i+j 부터 재귀 
        ans = []
        recursion(s, 0, []) # 첫 recursion : i == 0부터 시작
        return ans            

s1 = "catsanddog"
wordDict1 = ["cat","cats","and","sand","dog"]
s2 = "pineapplepenapple" 
wordDict2 = ["apple","pen","applepen","pine","pineapple"]
s3 = "catsandog"
wordDict3 = ["cats","dog","sand","and","cat"]

a = Solution()
print(a.wordBreak(s1, wordDict1))
