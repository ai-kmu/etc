class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        cur_h = 0
        min_rungs = 0

        for r in rungs:
            if (r - cur_h) > dist:
                min_rungs += (r - cur_h - 1) // dist
            
            cur_h = r

        return min_rungs
