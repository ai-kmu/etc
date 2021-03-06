class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1
        maxList = [0] * (n+1)     

        for i in range(2, n+1):
            for j in range(1, i):
                maxList[i] = max(maxList[i], max(j*(i-j), j*maxList[i-j]))
                # maxList[i]는 합 구성이 원소 두개로, 뒷 부분은 합구성이 원소 세개 이상일 경우
               
        return maxList[n];
        
