from collections import deque

class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        temp = []
        queu_s = deque(s)
        queu_g = deque(goal)
        
        ans = ''
        for i in range(len(queu_s)+1):
            now = queu_s.popleft()
            queu_s.append(now)
            if queu_s == queu_g:
                return True
        
        return False
