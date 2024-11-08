class Solution:
    def isHappy(self, n: int) -> bool:
        check_list = [n]
        while n != 1:
            # print(n)
            temp = 0
            
            while n:
                a = n % 10
                temp += a**2
                n = n // 10

            n = temp

            if n in check_list:
                return False

            check_list.append(n)

        return True

        

