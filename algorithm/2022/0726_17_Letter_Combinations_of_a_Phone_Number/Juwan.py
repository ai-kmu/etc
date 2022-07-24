from itertools import product # Python 공식 Document에도 있음. 순열 및 조합 문제에 코테에서도 충분히 쓸 수 있는 라이브러리인듯.

class Solution:
  
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits: # 아무것도 없는 case에 대한 처리
            return []
        
        keypad = {'2':'abc',
                 '3':'def',
                 '4':'ghi',
                 '5':'jkl',
                 '6':'mno',
                 '7':'pqrs',
                 '8':'tuv',
                 '9':'wxyz'} # 번호판 키패드 구현
        
        for_iter = [] # iter tools를 위해 만드는 리스트
        
        answer = []
        
        for i in digits:
            for_iter.append(list(keypad[i])) # 조합 돌릴 알파벳들을 담음. [['a', 'b', 'c'], ['d', 'e', 'f']]
        
        for i in product(*for_iter, repeat=1):
            answer.append(''.join(i))
        
        return answer
