class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        answer = []
        tmp = []
        
        def findWord(start, tmp, res):
            
            # 만약 탐색 시작 지점이 s의 길이보다 길면 
            # tmp 배열의 원소들을 join 후 return
            if start == len(s):
                res.append(' '.join(tmp))
                return
            
            word = ''
            for i in range(start, len(s)):
                word += s[i]
                
                # start 지점 이후로 생성된 단어가 wordDict에 존재하면
                if word in wordDict:
                    tmp.append(word)
                    
                    # 생성된 단어 이후 지점을 start로 설정해주고 탐색
                    findWord(i+1, tmp, res)
                    #print(tmp)
                    #print(start)
                    tmp.pop()
        
        
        findWord(0, tmp, answer)
        return answer
