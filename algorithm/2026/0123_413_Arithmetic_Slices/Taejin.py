class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # diff 같은거 끼리 split = maximum arithmetic subsequence length
        # Num of arithmetic subsequence = len(arithmetic sequence) - 1 C 2 = d(d - 1) / 2
        # 또는 maximum arithmentic length로부터 diff 길이가 2가 될 때까지 줄여나가면 1 + 2 + ... + len(arithmetic sequence) - 1 = d(d - 1)/2
        if len(nums) < 3:
            return 0
        
        diff = []
        dummy = nums[1] - nums[0]
        cnt = 1
        for i in range(1, len(nums) - 1): # diff 같은거끼리 split -> maximum arithmetic subsequence length 계산
            if dummy != nums[i + 1] - nums[i]:
                diff.append(cnt)
                dummy = nums[i + 1] - nums[i]
                cnt = 0
            cnt += 1

        diff.append(cnt) # 마지막 maximum arithmetic subsequence length append

        return sum([(d * (d - 1)) // 2 for d in diff])
