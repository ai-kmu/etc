from collections import defaultdict
from string import ascii_lowercase

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []
        
        # 정답 리스트
        answer = []
        # 알파벳 리스트
        alphabet_list = list(ascii_lowercase)
        # 알파벳 chunk 리스트
        alphabet_chunk_list = []
        # phone number dictionary(hash)
        phone_number = defaultdict()
        
        # 알파벳 chunk list 생성
        for i in range(0,8):
            alphabet_chunk = []
            if i == 7 or i == 9:
                size = 4
            else:
                size = 3
            for j in range(size):
                if i >= 8:
                    alphabet_chunk.append(alphabet_list[3*i+j+1])
                else:
                    alphabet_chunk.append(alphabet_list[3*i+j])
            alphabet_chunk_list.append(alphabet_chunk)
            
        # 만들어진 알파벳 chunk 활용하여 phone number dictionary 만들어줌
        for key, value in enumerate(alphabet_chunk_list):
            phone_number[str(key+2)] = value
        
        # 재귀 활용하여 조합 구함
        def backtrack(i, str):
            # str의 길이와 digits의 길이가 같아지면 재귀 완료
            if len(digits) == len(str):
                answer.append(str)
                return answer
            # digits마다 계속 알파벳 더해줌
            for c in phone_number[digits[i]]:
                backtrack(i+1, str + c)
        
        backtrack(0,"")
        
        return answer
