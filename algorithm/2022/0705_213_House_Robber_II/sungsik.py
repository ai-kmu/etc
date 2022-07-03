class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        # n이 3이하일 경우 최댓값이 정답
        if n <= 3:
            return max(nums)
        
        # nums의 모든 위치에서 시작하여 한칸씩 시계방향으로 확장해가며 최댓값을 구함
        # dp[k][l] => l번째 위치에서부터 k개의 위치를 사용했을 때의 최댓값
        dp = [[0] * n for _ in range(n)]
        # 마지막을 추가할 때는 시작 위치에서의 사용 여부를 기억해야함
        first_used = [True] * n
        
        # base case
        # 0번쨰는 nums와 동일
        dp[0] = nums.copy()
        
        # 1번째는 현재 위치에서 한칸 옆에 있는 것과의 최댓값과 동일
        for i in range(n):
            if nums[(i+1)%n] > nums[i]:
                dp[1][i] = nums[(i+1)%n]
                # 만약 한칸 옆에 있는 것이 최댓값이면 first_used를 False로 설정
                first_used[i] = False
            else:
                dp[1][i] = nums[i]
        
        # 2번쨰는 0번째 + 2번째와 1번째의 최댓값으로 설정
        # 0번째 + 2번째로 설정할 경우 first_used를 True로 설정
        for i in range(n):
            if nums[(i+2)%n] + nums[i] > nums[(i+1)%n]:
                dp[2][i] = nums[(i+2)%n] + nums[i]
                first_used[i] = True
            else:
                dp[2][i] = nums[(i+1)%n]
        
        # 3번째부터는 i번째 옆에 있는 것을 사용하는 경우와 사용하지 않은 경우로 구함
        for i in range(3, n):
            for j in range(n):
                # 마지막 단계에서 처음을 사용했을 경우 넘어감
                if i == n-1 and first_used[j]:
                    continue
                dp[i][j] = max(dp[i-2][j] + nums[(j+i)%n], dp[i-1][j])
        
        return max([max(row) for row in dp])
