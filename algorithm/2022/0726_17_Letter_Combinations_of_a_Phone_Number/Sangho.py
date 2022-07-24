# 곱집합(product)를 사용하기 위해 import
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # 예외 사항 (문제에서의 example 2)
        if digits == "":
            return []
          
        # 문제 풀이중 list를 임시로 저장할 빈 list 생성
        temp = []
        
        # 각 자판에 해당하는 string list를 dict 형태로 저장
        num_dict = {
            "2" : ['a', 'b', 'c'],
            "3" : ['d', 'e', 'f'],
            "4" : ['g', 'h', 'i'],
            "5" : ['j', 'k', 'l'],
            "6" : ['m', 'n', 'o'],
            "7" : ['p', 'q', 'r', 's'],
            "8" : ['t', 'u', 'v'],
            "9" : ['w', 'x', 'y', 'z'],    
        }
        
        # input으로 들어온 digits의 각 숫자 자판에 해당하는 string을 list로 임시 저장
        for digit in digits:
            temp.append(num_dict.get(digit))
            
        # 임시 저장한 temp list의 내용물들을 product하여 모든 가능한 조합 뽑기
        temp_prod = list(product(*temp))
        
        # output을 원하는 형태로 변환.
        return ["".join(temp_prod[i]) for i in range(len(temp_prod))]
