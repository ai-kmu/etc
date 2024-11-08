class Solution:
    def isHappy(self, n: int) -> bool:
        cnt = 999

        def split_function(n):
            result = []
            for i in range(len(str(n))):
                result.append(int(str(n)[i]))
            return result

        while n != 1:
            cnt -= 1
            if cnt == 0:
                return False
            value_list = split_function(n)
            n = 0
            for i in value_list:
                n += i**2
                
        return True
