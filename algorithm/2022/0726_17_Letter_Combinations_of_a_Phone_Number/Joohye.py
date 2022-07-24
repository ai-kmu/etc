class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 딕셔너리 선언
        d = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
        
        # digits 안의 값이 숫자가 든 경우, 빈 경우 구분
        d_lst =[]
        if digits:
            d_lst = ['']
        else:
            []
        
        for num in digits:
            temp = []
            # 조합가능한 수를 d_lst에서 뽑아서
            for word in d_lst:
                # 각 digit 별로 조합 가능한 수를 뽑아서
                for letters in d[int(num)]:
                    # 두 조합을 append 한 후 temp에 저장
                    temp.append(word + letters)
                   
            d_lst = temp
        return d_lst
        
