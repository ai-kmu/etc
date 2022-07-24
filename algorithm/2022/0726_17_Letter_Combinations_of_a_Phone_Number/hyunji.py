class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        answer = []
        buttons = {"2" : 'abc', "3" : 'def', "4" : 'ghi', "5" : 'jkl', 
                   "6" : 'mno', "7" : 'pqrs', "8" : 'tuv', "9" : 'wxyz'}
        
        if digits == "":
            return []
        
        def combinations(idx, letter): 
            # 하나의 조합이 완성되면 return
            if len(digits) == len(letter):
                # 완성된 조합 정답 배열에 append
                answer.append(letter)
                return
            
            # 현재 번호(key)에 해당하는 문자(value) 탐색
            for c in buttons[digits[idx]]:
                # 다음 번호 탐색, letter에 현재 번호의 문자 추가
                combinations(idx+1, letter+c)
                
        combinations(0,"")
        return answer
