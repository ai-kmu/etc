class Solution(object):
    
    # 배열의 최대 sub array 합을 구하기 위한 함수 
    def findMaxSum(self, arr):
        maxSum = arr[0]
        tempMax = 0
        
        # 역대 최대값은 maxSum에 저장시키고 각 숫자를 tempMax에 더해준다 
        for each in arr:
            tempMax += each
            
            # 더해준 값이 0보다 작다면 0으로 변경
            if tempMax < 0:
                tempMax = 0
            
            # 새로 더한 값이 역대 최대 값보다 크다면 역대 최대값을 갱신 시켜준다
            if maxSum < tempMax:
                maxSum = tempMax
        
        return maxSum 
    
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        # k가 1인 경우 
        if k == 1:
            return self.findMaxSum(arr) % (pow(10, 9) + 7)
 
        else:
            # 배열에 모두 양수만 들어있을 때 최대값을 k번 곱해준다 
            if min(arr) > 0:
                return (self.findMaxSum(arr) * k) % (pow(10, 9) + 7)
            # 배열에 음수가 섞여있을 때 
            else:
                '''
                힌트 4번에 나와있는 이 부분이 들어가야하는 것 같은데.. 구현 실패
                the maximum suffix sum plus the maximum prefix sum plus (k-2) multiplied by the whole array sum for k > 1.
                '''
                return 0
            
    
    
