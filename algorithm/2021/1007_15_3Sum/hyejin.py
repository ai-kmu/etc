class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # i != k , i !=j, j!= k를 만족하면서 합이 0인 index i, j, k의 집합을 만들자
        
        if len(nums) < 3: # 3개 미만일때
            return []
        
        triplets = set()
        
        nums = sorted(nums) # nums 정렬
        
        # triplet을 못만드는 경우, 0만 있는 경우
        if (nums[0] < 0 and nums[-1] <= 0) or (nums[0] >= 0 and nums[-1] > 0):
            return []
        elif nums[-1] == 0 and nums[0] == 0:
            return [[0,0,0]]
        
        for i in range(len(nums)): # 모든 경우의 수 찾기
            left = i + 1 # i, j, k는 같지 않기 때문에 i 다음부터 찾기 시작
            right = len(nums) - 1
            while left < right: # left < right일 때까지
                triplet_sum = nums[i] + nums[left] + nums[right] 
                if triplet_sum == 0:
                    triplets.add((nums[i], nums[left], nums[right]))
                    right -= 1
                elif triplet_sum < 0: # 음수쪽의 합이 더 크기 때문에 음수를 줄여줌.
                    left += 1
                else: # 양수쪽의 합이 더 크기 때문에 양수를 줄여줌
                    right -= 1
                    
        return list(triplets)
