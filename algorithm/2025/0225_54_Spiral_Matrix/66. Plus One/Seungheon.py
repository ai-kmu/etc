class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # 맨 뒤에 1 더하기
        carry = 1
        for i in range(len(digits)):
            idx = -i - 1
            
            # 넘어가면
            if digits[idx] + carry > 9:
                digits[idx] = 0
                if i == len(digits) -1:
                    digits = [1] + digits
            else:
                digits[idx] += carry
                break
            

        return digits
