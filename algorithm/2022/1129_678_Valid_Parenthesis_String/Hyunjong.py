class Solution:

    # 왼쪽 괄호 개수 min, max값을 구해 판단하기
    # *은 ( ) 혹은 빈 문자 가 될 수 있기 때문에 최소 최대로 풀기 가능하다
    def checkValidString(self, s: str) -> bool:
        num_l_min = 0
        num_l_max = 0

        for char in s:
                
            if char == '(':
                num_l_min += 1
                num_l_max += 1

            elif char == ')':
                num_l_min -= 1
                num_l_max -= 1

            # char == *
            else:
                num_l_min -= 1
                num_l_max += 1

            num_l_min = max(0, num_l_min)

            if num_l_max < 0: 
                return False

        if num_l_min == 0:
            return True
        else:
            return False
