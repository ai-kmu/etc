class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        num = []
        temp = []

        while True:
            if n // k < k:
                num.append(n//k)
                num.append(n % k)
                n = n//k
                break
            else:
                temp.append(n % k)

                n = n//k

                
        return(sum(num+temp))
        


                
            
