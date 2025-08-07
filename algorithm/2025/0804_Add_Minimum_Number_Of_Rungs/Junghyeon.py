class Solution(object):
    def addRungs(self, rungs, dist):
        """
        :type rungs: List[int]
        :type dist: int
        :rtype: int
        """
        rungs = [0] + rungs
        ans = 0
        for i in range(len(rungs)-1, 0, -1):
            prev_climb = rungs[i-1] + dist
            if prev_climb >= rungs[i]:
                continue
            else:
                if (rungs[i] - rungs[i-1]) % dist > 0: 
                    ans += (rungs[i] - rungs[i-1]) // dist
                else:
                    ans += (rungs[i] - rungs[i-1]) // dist
                    ans -= 1
                    
        return ans
