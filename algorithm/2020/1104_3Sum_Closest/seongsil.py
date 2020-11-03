class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = []
        nums.sort()

        closest_sum = 10**3 * 3
        sum_ = 0
        if len(nums) == 3:
            return sum(nums)
        for a in range(len(nums)-1):
            b = a + 1
            c = len(nums)-1
            while b < c:
                sum_ = nums[a]+nums[b]+nums[c]  # 세 수의 합
                if sum_ == target:  # sum이 target과 같으면 스탑
                    closest_sum = sum_
                    break                
                elif sum_ < target:
                    b += 1
                elif sum_ > target:
                    c -= 1

                if abs(sum_ - target) < abs(closest_sum - target):     # target과의 차이가 적으면 closest_sum 갱신              
                    closest_sum = sum_
                    
            if sum_ == target:
                break
                    

                
        return closest_sum
