from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 입력한 숫자가 없으면 빈 list 반환
        if not digits:
            return []
        # 딕셔너리에 해당하는 키패드 저장
        keypads = {'2' : ['a','b','c'],
                   '3' : ['d','e','f'],
                   '4' : ['g','h','i'],
                   '5' : ['j','k','l'],
                   '6' : ['m','n','o'],
                   '7' : ['p','q','r','s'],
                   '8' : ['t','u','v'],
                   '9' : ['w','x','y','z']
                  }
        nums = []
        output = []
        # 입력한 숫자에 해당하는 키패드 뭉치 추가
        for i in digits:
            nums.append(keypads[i])
        # product를 통해 리스트의 모든 조합을 구함
        for i in list(product(*nums)):
            # string의 형태로 추가하기 위해 temp에다가 각각의 조합을 추가해서 output에 append
            temp = ""
            for j in i:
                temp += j
            output.append(temp)
        return output
