class Solution:
    def fillCups(self, amount: List[int]) -> int:
        s = sum(amount)
        ss = sorted(amount, reverse=True)
        
        cnt = 0

        while ss[1] != 0 and ss[2] != 0 and ss[0] != 0:
            if ss[1] > ss[2]:
                cnt += 1
                ss[0] -= 1
                ss[1] -= 1
            else:
                cnt += 1
                ss[0] -= 1
                ss[2] -= 1

        return cnt + max(ss)
