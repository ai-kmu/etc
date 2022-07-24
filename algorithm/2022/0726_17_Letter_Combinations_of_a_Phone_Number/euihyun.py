# 조합 생성용
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp = []
        ans = []
        # 해쉬맵 생성
        dic = {2:['a','b','c'], 3:['d','e','f'],
               4:['g','h','i'], 5:['j','k','l'],
               6:['m','n','o'], 7:['p','q','r','s'], 
               8:['t','u','v'], 9:['w','x','y','z']}
        # 비어있으면 리턴
        if digits == "":
            return []
        
        # digits 에 해당되는 값들 리스트에 추가
        for i in digits:
            temp.append(dic.get(int(i)))
        
        # temp안에 있는 리스트들 조합 생성
        # join으로 붙이고 ans에 추가
        for i in list(product(*temp)):
            ans.append("".join(i))
        
        return ans
                

    

            
        

        
