class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        

        for i in range(len(s)):
            new_s = s[1:] + s[0]
            # print(new_s)
            if new_s == goal:
                return True
            s = new_s
        return False
