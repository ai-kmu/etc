class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        answer = []
        hashWord = []
        
        for _ in wordDict:
            if s.find(_) != -1:
                hashWord.append(_)
        
        for _ in hashWord:
            a = ''
            cnt = s.count(_)
            while cnt:
                a += s.replace(s, '')
                cnt -= 1
        
        print(a)
                
                
