# 1. 우선 nums를 정렬한다.
# 2. 그 후 완전 탐색으로 앞에서 부터 2개를 선택한다. (choose i, j)
# 3. nums[j:]에서 target - nums[i] - nums[j]가 가능한 것들이 있는지 탐색한다.


class Solution:
    def fourSum(self, nums, target):
        
        # target - nums[i] - nums[j]를 찾음
        def twosum(nums, target):
            l,r = 0,len(nums)-1
            ans = []
            while(l < r):
                if nums[l] + nums[r] < target:
                    l+=1
                elif nums[l] + nums[r] > target:
                    r-=1
                else:
                    ans.append([nums[l], nums[r]])
                    l+=1
                    r-=1
                    
            return ans
        
        nums.sort()
        count = []
        # 앞에서 부터 2개의 숫자는 완전 탐색으로 찾음
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                two_list = twosum(nums[j+1:], target-nums[i]-nums[j])
                for l in two_list: # 찾은 list들을 ans에 추가해줌
                    count.append([nums[i], nums[j]] + l)
                        
        return list(set(map(tuple,count))) # 중복 제거
