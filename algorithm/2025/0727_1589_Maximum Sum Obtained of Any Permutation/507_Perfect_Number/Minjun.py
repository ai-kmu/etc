class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        st = 2
        ed = num//2
        cand = [1]
        while st < ed:
            if num % st == 0:
                ed = int(num / st )
                cand.append(int(st))
                cand.append(int(ed))
            st += 1
        if sum(cand) == num:
            return True
        return False

