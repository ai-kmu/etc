class Solution(object):
    def isHappy(self, n):
        visited = set()
        n = str(n)
        while True:
            total = 0
            for i in n:
                total += int(i)**2
            if total in visited:
                return False
            if total == 1:
                return True
            visited.add(total)
            n = str(total)
