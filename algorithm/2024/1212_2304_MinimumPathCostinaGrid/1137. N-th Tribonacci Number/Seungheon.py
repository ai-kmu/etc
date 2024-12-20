class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_list = [0,0,1]

        if n == 0:
            return 0
        for _ in range(n):
            tmp = sum(num_list)
            num_list[0] = num_list[1]
            num_list[1] = num_list[2]
            num_list[2] = tmp

        return num_list[1]
