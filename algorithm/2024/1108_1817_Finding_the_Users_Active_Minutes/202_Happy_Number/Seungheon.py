class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while 1 :
            print(n)
            if len(str(n)) == 1:
                if n == 1:
                    return True
                elif n == 7:
                    return True
                else:
                    return False
            
            new_n = 0
            for i in str(n):
                new_n += int(i)*int(i)
            n = new_n
        return False
