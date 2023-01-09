# 등장 좌표로만 판단해보려고 온갖 수를 다 뒀지만 실패했음
# 참 어렵다 . . .
from collections import defaultdict
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        num_dict = defaultdict(int)
        xm, ym, amax, bmax = float("inf"), float("inf"), float("-inf"), float("-inf")
        for x,y,a,b in rectangles:
            num_dict[x] += 1
            num_dict[y] += 1
            num_dict[a] += 1
            num_dict[b] += 1
            if x < xm:
                xm = x
            if y < ym:
                ym = y
            if a > amax:
                amax = a
            if b > bmax:
                bmax = b
        ans = sum(num_dict.values())
        odd = 0
        even = 0

        if num_dict[xm] % 2 != 0:
            odd += 1
        if num_dict[ym] % 2 != 0:
            odd += 1
        if num_dict[amax] % 2 != 0:
            odd += 1
        if num_dict[bmax] % 2 != 0:
            odd += 1
        a = num_dict.values()
        ans -= num_dict[xm]
        ans -= num_dict[ym]
        ans -= num_dict[amax]
        ans -= num_dict[bmax]
        for _ in a:
            if _ % 2 == 0:
                even += 1
        if ans % 2 == 0 and odd == 2:
            return True
        return False

