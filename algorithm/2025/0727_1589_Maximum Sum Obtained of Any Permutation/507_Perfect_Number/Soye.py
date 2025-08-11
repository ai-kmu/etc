class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1 : 
            return False
        
        tmp = 1
        
        for i in range(2, int(math.sqrt(num))+1) :
            if num % i == 0 :
                tmp += i + num//i

        return tmp == num
