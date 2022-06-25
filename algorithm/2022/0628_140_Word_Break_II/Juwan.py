class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        answer = []
        """
        catsanddog
        
        -> cat / sanddog -> cat / sand / dog -> [cat, sand, dog] = 문장 끝에 도달했을 때 remain에 담긴 것들
        
        -> cats / anddog -> cats / and / dog -> [cats, and, dog]
       
        """
        
        
        
        def partioning(string, remain):
            
            if not string: # 문장 끝에 도달했을 때, remain에 들어있는 모든 word와 그 사이에 공백을 넣어 join.
                answer.append(' '.join(remain))
                
            else: # 아직 안끝났다면
                
                for word in wordDict:
                    
                    if string[:len(word)] == word: # 검증과정. 즉, 딕셔너리에 존재하는 word로 검사해봤을 때,
                                                   # 
 
                        temp = copy.deepcopy(remain)
                        temp.append(word)
                        partioning(string[len(word):], temp)
        
        partioning(s, [])
        
        return answer
