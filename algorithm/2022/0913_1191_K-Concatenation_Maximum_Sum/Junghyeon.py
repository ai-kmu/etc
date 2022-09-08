class Solution:
    '''
    len(arr) * k 만큼의 dp 테이블을 생성하면 시간초과가 발생한다.
    배열에서 최댓값을 가질 수 있는 모든 경우의 값를 계산해서 그 중 최댓값을 골라준다.
    '''
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # arr을 뒤집은 배열을 새로 생성
        rev_arr = arr[::-1]
        
        # dp : k=1일때 arr에 대한 dp 테이블
        dp = [0] * len(arr)
        dp[0] = arr[0]
        
        # prefix : arr에서 누적 합을 기록하는 테이블
        prefix = [0] * len(arr)
        prefix[0] = arr[0]
        
        # suffix : rev_arr에서 누적 합을 기록하는 테이블
        suffix = [0] * len(rev_arr)
        suffix[0] = rev_arr[0]
        
        # dp 테이블을 채워준다.
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
        
        # prefix의 테이블을 채워준다.
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + arr[i]
            
        # suffix의 테이블을 채워준다.
        for i in range(1, len(suffix)):
            suffix[i] = suffix[i-1] + rev_arr[i]
        
        # 첫번째 경우 : 모든 값을 더했을 때 최대인 경우
        a = sum(arr) * k
        
        # 두번쨰 경우 : 미리 구한 dp 테이블에서의 최댓값
        # k = 1이면 dp 테이블에서만 최댓값을 가지지만, k > 1인 경우 또다른 arr가 존재한다.
        # 마지막 원소 == dp 테이블의 최댓값인 경우, prefix 테이블에서의 최댓값을 더해주어야한다.
        # 첫번째 원소 == dp 테이블의 최댓값인 경우, suffix 테이블에서의 최댓값을 더해주어야한다.
        if max(dp) == dp[-1] and k > 1:
            b = max(dp) + max(prefix)
        elif max(dp) == dp[0] and k > 1:
            b = max(dp) + max(suffix)
        else:
            b = max(dp)
        
        # 세번째 경우 : n = 1, n = k 일때를 제외한 나머지 배열의 합 + prefix의 최댓값 + suffix의 최댓값
        # 네번째 경우 : prefix의 최댓값 + suffix의 최댓값
        if k > 1:
            c = max(suffix) + max(prefix) + sum(arr)*(k-2)
            d = max(suffix) + max(prefix)
        else:
            c = 0
            d = 0
            
        # 앞선 네가지의 경우와 0 중에서 최댓값을 결과값으로 저장
        result = max(0, a, b, c, d)
        
        return result % (10**9 + 7)
