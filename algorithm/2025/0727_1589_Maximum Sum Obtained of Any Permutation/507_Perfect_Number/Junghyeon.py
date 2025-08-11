class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False

        sq = int(num ** 0.5)

        s = 1

        for i in range(2, sq+1):
            if num % i == 0:
                t = num//i
                s += t+i

        if s == num:
            return True

        return False
