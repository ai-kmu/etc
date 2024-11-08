class Solution(object):
    def isHappy(self, n):
        
        result = 0
        sums = 0
        x = 0

        while True:
            for i in str(n):
                sums += int(i) ** 2
                print(i)
            if sums == 1:
                result = 1
                break
            elif x >= 100:
                break
            else: 
                n = sums
                x += 1
                sums = 0
        
        return result == 1