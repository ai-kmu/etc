class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_str = [i for i in s]
        t_str = [i for i in t]
        s_str.sort()
        t_str.sort()
#         print(s_str, t_str)
        for i in range(len(t_str)):
            try:
                if t_str[i] != s_str[i]:
                    return t_str[i]
            except:
                return t_str[i]
