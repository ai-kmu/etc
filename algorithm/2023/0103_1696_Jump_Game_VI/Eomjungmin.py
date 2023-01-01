class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums) # n: nums 길이 저장

        # 동적 프로그래밍을 이용하기 위해 dp list 선언
        dp = [0] * n
        dp[0] = nums[0]

        # 동시에 deque를 이용하여 dp 구할 때 최대값을 가지게 하는 인덱스 저장하도록 함
        dq = deque()
        dq.append(0)

        for i in range(1, n):
            '''          
            처음 dp[i]값 계산
            dq[0]: k 범위 안에서 더해야 하는 후보들 중에 최대값을 가지게 하는 인덱스
            업데이트 방식은 밑에
            '''
            dp[i] = nums[i] + dp[dq[0]]
            
            '''         
            현재 i에서 왼쪽으로 k만큼 이동했을 때의 값이
            현재 deque[0]에 저장하는 값보다 크면 
            기존 deque[0]의 값을 pop
            이유: i에서 왼쪽으로 k만큼 보므로
            '''
            if dq[0] < i-k+1: 
                dq.popleft()
            
            '''
            deque에 저장된 가장 큰 인덱스 값에 해당되는 dp값이랑
            dp[i]랑 비교하여 dp[i]가 더 크면
            dq의 맨 마지막 값을 pop
            이유: deque 업데이트. dq에서 인덱스 0은 다음 i+1의 dp값을 구할 때 최대로 가지게 하는 인덱스
            '''
            while dq and dp[dq[-1]] < dp[i]:
                dq.pop()
            dq.append(i)

        return dp[-1]
