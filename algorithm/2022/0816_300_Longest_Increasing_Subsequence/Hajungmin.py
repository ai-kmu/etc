class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # n이 1일 경우 길이가 1이므로 예외처리
        if n == 1 : return 1

        # 배열에 0을 추가해서 dp와 인덱스를 맞춰줌
        # dp도 n보다 1크게 생성
        nums.insert(0,0)
        dp = [0]*(n+1)
        
        # dp 1번 인덱스는 길이가 1이므로 1로 초기화 
        dp[1] = 1
        answer = 0
        
        # 배열의 첫 번째 수는 1이고 두 번째 수는 인덱스 2부터 시작
        # 따라서 루프를 2부터 돌기 시작
        for i in range(2, n+1):
            
            # dp에서 가장 긴 길이를 찾아 저장하는 변수 선언
            max_len = 0
            
            # 현재 인덱스의 앞쪽에서 가장 긴 길이의 시퀀스를 이루는 것을 탐색
            for j in range(i-1, 0, -1):
                
                # 만약 배열에서 현재 본인보다 작은 수를 dp에서 찾았을 때
                # 현재 max_len보다 크다면 max_len을 바꿔줌
                if nums[j] < nums[i] and dp[j] > max_len:
                    max_len = dp[j]
            
            # 바뀐 max_len에 현재 본인까지 더해서 1을 증가시킨 후 dp 업데이트
            dp[i] = max_len + 1
            
            # 만약 answer가 현재 dp값보다 작을 경우 answer 업데이트
            if dp[i] > answer:
                answer = dp[i]
        
        return answer
