class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set() # 결과 셋
        nums.sort() # 들어온 값을 우선 정렬함
        for i in range(len(nums)): # sort된 nums에서 첫 요소부터 탐색 시작
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j , k = i + 1, len(nums) -1 # left와 right
            while j < k :
                temp_sum = nums[i] + nums[j] + nums[k]
                if temp_sum > 0: k -= 1 # 합이 0보다 크면 보다 더 작은 값을 더하기 위해 k -= 1로 오른쪽을 앞으로 당김
                elif temp_sum < 0: j += 1 # 그 반대로 0보다 작으면 더 큰 값을 더하기 위해 왼쪽을 뒤로 당김
                else:
                    result.add((nums[i], nums[j], nums[k])) #값이 0에 맞아 떨어진다면 더함.
                    j += 1 # 범위를 좁
                    k -= 1
        return list(result)
