    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque([0])  # nums의 인덱스를 저장하되 내림차순 순으로 저장시켜야됨
        for i in range(1, n):
            # nums[i] = max(nums[i-k], nums[i-k+1],.., nums[i-1]) + nums[i]
            nums[i] = nums[dq[0]] + nums[i]
            
            # nums[i]를 deq에 추가
            while dq and nums[dq[-1]] <= nums[i]: 
                dq.pop()  # nums[i]보다 작거나 같은 원소 제거
            dq.append(i) 
            # 마지막 원소가 k 사이즈를 넘어가면 제거
            
            if i - dq[0] >= k: 
                dq.popleft()

        return nums[n - 1]
