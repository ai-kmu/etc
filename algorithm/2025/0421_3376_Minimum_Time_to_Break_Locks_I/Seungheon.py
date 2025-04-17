# fail code

class Solution(object):
    def findMinimumTime(self, strength, k):
        """
        :type strength: List[int]
        :type k: int
        :rtype: int
        """
        
        strength.sort()  
        time = 0 
        x = 1
        for s in strength:
            energy = 0
            while energy < s:
                time += 1
                energy += x
            x += k 
        return time
