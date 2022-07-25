'''
    데카르트 곱(product 연산) 구현해보고 싶어서 직접 해봤습니다.    
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # trivial case
        if not digits:
            return
        
        # telephone button
        digit = {}
        ascii_a = 97

        # telephone button 생성
        for i in range(2, 10):
            if i == 7 or i == 9:
                digit[i] = [chr(ascii_a), chr(ascii_a+1), chr(ascii_a+2), chr(ascii_a+3)]
                ascii_a += 4
                continue
            
            digit[i] = [chr(ascii_a), chr(ascii_a+1), chr(ascii_a+2)]
            ascii_a += 3
        
        # trivial case
        if len(digits) == 1:
            return digit[int(digits)]
        
        # 데카르트 곱 구현(itertools - product 연산)
        # 두 리스트의 중복되지 않는 요소곱 return
        # arr1, arr2: 연산 대상
        # idx: 다음 recursion의 arr2 지정
        #     ex) input list 요소 예
        #        1. digits[0], digits[1], 1  --output--> tmp
        #        2.   tmp, digits[2], 2(idx(1)+1)  --output--> tmp
        #        3.   tmp, digits[3], 3(idx(2)+1)  --output--> tmp
        def recursion(arr1, arr2, idx):
            tmp = []
            # arr1 & arr2 데카르트 곱
            for i in arr1:
                for j in range(len(arr2)):
                    # 연산결과 tmp에 update
                    tmp.append(i + arr2[j])
            
            # 다음 digits 요소 있는지 체크
            # 있다면 tmp와 다음 digits 요소인 idx+1으로 recursion 호출
            if idx+1 < len(digits):
                return recursion(tmp, digit[int(digits[idx+1])], idx+1)
            # 다음 요소 없다면, 연산 결과 return
            return tmp
        
        # digits 0, 1번째 요소부터 데카르트 곱 시작
        return recursion(digit[int(digits[0])], digit[int(digits[1])], 1)
