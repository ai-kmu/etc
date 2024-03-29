# 구현에 실패하여 정답을 보고 공부하였습니다.
# 정답을 보고 했기에 리뷰해주지 않아주셔도 됩니다.
# 늦게올려 죄송합니다.
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        '''
        문제 풀이
        배열내 앞&뒤 에서의 최대부분합을 이용하면 됩니다.
        1. 만약 배열의 합이 0보다 큰 경우: 최대한 많이 반복하는게 이득
            1) k = 1 인경우: 배열 내의 최대부분 합
            2) k = 2 인경우: 배열 내 앞에서부터 최대부분합 + 뒤에서부터 최대부분합
            3) 그 외의 경우: 배열 내 앞에서부터 최대부분합 ~ 뒤에서부터 최대부분합(중간 다더해줌)
        2. 배열의 합이 0보다 작은 경우
            1) 모두 음수면 0(안더해준 경우에 대하여)
            2) 배열 내의 최대부분 합
        '''
    def maxSubarray(self, A):
        # A는 k가 적용된 배열
        if not A: # 모두 음수면 0
            return 0 
        curSum = A[0]
        maxSum = A[0]
        '''
        ex1의 경우
        모든 더한값이 0보다 크고, k가 2보다 크므로
        맨 앞의 배열 ~ 맨 뒤의 배열의 합을 구합니다.('~'는 사이의 전체 합을 더해준다는 의미입니다.)
        '''
        for i in range(1, len(A)):
            curSum = max(A[i], curSum + A[i])
            maxSum = max(curSum, maxSum) 
            print(maxSum)        
        return max(maxSum,0)
        
    def kConcatenationMaxSum(self, arr, k):
        arrSum = sum(arr)
        MOD = (10**9 + 7) # 정답이 너무 커지는 경우에 대한 예외처리
        if k == 1: # 풀이의 k가 1인 경우
            return self.maxSubarray(arr)%MOD
        if k == 2: # 풀이의 k가 2인경우
            return self.maxSubarray(2*arr)%MOD
        if k > 2 and arrSum > 0: # 풀이의 그외의 경우
            return (self.maxSubarray(arr+arr) + (k-2)*arrSum)%MOD
        else: # 배열의 합이 0보다 작은 경우
            return self.maxSubarray(2*arr)%MOD
