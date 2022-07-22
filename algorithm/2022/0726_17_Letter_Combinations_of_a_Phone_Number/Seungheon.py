from collections import defaultdict
from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        
        # 예외처리
        if not digits:
            return []

        # dictionary만들기
        key_dict = defaultdict(list)
        k=0
        for i in range(2,10):
            if i > 7:
                k = 1
            # 7, 9에서는 4개
            for j in range(3 if i!=7 and i!=9 else 4):
                key_dict[i].append(chr(91+3*i+j+k))
        
        # 숫자로 입력가능한 글자 모음 list
        nums = [key_dict[int(num)] for num in digits] 
        
				# 조합 구하기
        return list(map(lambda x : ''.join(x), list(product(*nums))))
