class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        no_reverse = [i for i in str(x)]
        temp = [i for i in str(x)]
        temp_reverse = []

        temp.reverse()

        if no_reverse == temp:
            return True
        else:
            return False
        
        
