class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        temp = s.split(' ')
        ans = ''
        ans_ = []
        for i in range(len(temp)-1,-1,-1):
            if temp[i] != '':

                ans_.append(str(temp[i]))
        
        for i in range(len(ans_)):
            if i != len(ans_)-1:
                ans += ans_[i]
                ans += ' '
            else:
                ans += ans_[i]
        
        return ans
        
