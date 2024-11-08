class Solution:
    def isHappy(self, n: int) -> bool:
        current_val = n
        next_val = 0
        cnt = 1
        
        while cnt < 100:
            while True:
                if current_val <= 0:
                    break

                next_digit = current_val % 10
                current_val = current_val // 10

                next_val += next_digit * next_digit

            cnt += 1
            if next_val == 1:
                return True
            else:
                current_val = next_val
                next_val = 0
        
        return False
