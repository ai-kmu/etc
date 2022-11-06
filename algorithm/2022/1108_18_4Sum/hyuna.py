class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 값 정렬 
        nums.sort()
        ans = []

        # i와 j는 고정해두고 안에 b와 e를 조정하며 타겟 값을 찾아나감
        # 정렬이 되어있기 때문에 타겟 값보다 작을때는 begin 값인 b를 늘려주고
        # 타겟 값보다 클 때는 end 값인 e를 줄여줌  
        for i in range(len(nums)):
            for j in range(i+1, len(nums)-1):
                b = j+1
                e = len(nums)-1

                while b < e:
                    # 합이 타겟값과 같을 때 
                    if nums[i] + nums[j] + nums[b] + nums[e] == target:
                        ans.append((nums[i], nums[j], nums[b], nums[e]))
                        b += 1
                        e -= 1
                    # 타겟 값보다 작을 때 
                    elif nums[i] + nums[j] + nums[b] + nums[e] < target:
                        b += 1
                    # 타겟 값보다 클 때 
                    else:
                        e -= 1
        
        # 중복 제거 후 리턴 
        return list(set(ans))
