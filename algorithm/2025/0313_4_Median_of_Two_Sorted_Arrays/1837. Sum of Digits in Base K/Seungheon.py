class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # n/k = carry .... namuge 
        # 100 / 6 = 16 ... 4
        # 16 / 6 = 2 ... 4
        answer = []

        carry = 101
        while k <= carry:
            carry = n // k
            namuge = n % k
            print(carry, namuge)
            answer.append(namuge)
            n = carry
        answer.append(n)
        return sum(answer)

        
