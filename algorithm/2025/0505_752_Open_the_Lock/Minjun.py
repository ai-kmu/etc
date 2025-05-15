# 못풀겠음.
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        cnt = 0

        def check_impossible():
            imp = [0] * 4
            for i in deadends:
                # 0
                if deadends[0] < target or deadends[0] > target:
                    imp[0] = True


        if check_impossible:
            return -1

        return cnt
