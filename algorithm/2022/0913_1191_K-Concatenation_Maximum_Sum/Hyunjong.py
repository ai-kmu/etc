# 실패, test case만 통과 
class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        arr = arr * k
        aws = 0    
        tmp = arr[0]
        num = len(arr)
        dp = [0] * num
        dp[0] = arr[0]
        flag = True
        
        for i in range(1, len(arr)):
            if arr[i] <0:
                flag = False
            
            dp[i] = max(arr[i], dp[i-1] + arr[i])
            if tmp != max(tmp, tmp + arr[i]):
                tmp = max(tmp, tmp + arr[i])
                if aws < tmp:
                    aws = tmp
            else:
                tmp = max(arr[i], 0)
                
        if k == 1 or flag:
            return max(dp +[0])
        return aws
