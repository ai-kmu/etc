class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 9가 아닐 땐 끝자리만 업데이트
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        
        # 9일 땐 .. 그냥 int로 다시 바꾸기 ㅋㅋ
        else:
            number = int(''.join(map(str, digits)))
            answer = number + 1
            return [int(i) for i in str(answer)]
