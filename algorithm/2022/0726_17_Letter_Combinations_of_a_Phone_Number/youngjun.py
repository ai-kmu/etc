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
        # phone number dictionary(hash)
        phone_number = {str(c):[] for c in range(2,10)}
        
        # phone number dictionary(hash) 생성
        for i in range(2,10):
            alphabet_chunk = []
            if i == 7 or i == 9:
                size = 4
            else:
                size = 3
            for j in range(size):
                if i >= 8:
                    phone_number[str(i)].append(alphabet_list[3*(i-2)+j+1])
                else:
                    phone_number[str(i)].append(alphabet_list[3*(i-2)+j])
        
        # 재귀 활용하여 조합 구함
        def recursion(i, str):
            # str의 길이와 digits의 길이가 같아지면 재귀 완료
            if len(digits) == len(str):
                answer.append(str)
                return answer
            # digits마다 계속 알파벳 더해줌
            for c in phone_number[digits[i]]:
                recursion(i+1, str + c)
        
        recursion(0,"")
        
        return answer
