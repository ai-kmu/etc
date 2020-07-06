class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        N = len(nums)
        arr = list(nums)
        # 가장 작은 원소를 arr에 넣음.
        for i in range(1,N):
            arr[i] = min(nums[i-1], arr[i-1])
    
        j = N
        # 거꾸로 for loop 돌음.
        for i in range(N)[::-1]:
            # nums와 arr를 비교했을 떄, arr이 더 크면 132는 아니므로 넘어감.
            if nums[i] <= arr[i]: 
                continue
            # j가 N보다 작고, arr j가 i보다 작을 때, j를 =1함.
            while j < N and arr[j] <= arr[i]:
                j += 1
            # j가 N보다 작고, arr[j]가 nums[i]보다 작을 떄, True를 냄.
            if j < N and arr[j] < nums[i]:
                return True
            # nums[i]가 arr[i-1]보다 클 때, j를 줄이고, arr[j]는 nums[i]로 할당함.
            if nums[i] > arr[i - 1]:
                j -= 1
                arr[j] = nums[i]

        return False
