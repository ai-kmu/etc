class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two pointer를 위해 정렬하는데, index 보존 위해 재정의 후에 정렬
        nums = [(n, i) for i, n in enumerate(nums)]
        nums.sort()
        print(nums)
        
        # 사용되는 two pointer
        left = 0
        right = len(nums) - 1
        
        # 탐색
        while left < right:
            # 현재 합 구하기
            _sum = nums[left][0] + nums[right][0]
            # 작으면 왼쪽 당기기
            if _sum < target:
                left += 1
            # 크면 오른쪽 당기기
            elif _sum > target:
                right -= 1
            # 같으면 정답인데, 기존 index를 반환해야함
            elif _sum == target:
                return [nums[left][1], nums[right][1]]
