# 정렬한 후 음수부와 양수부를 나눈다.
# 그 후 아래 case들을 모두 합집합한다.
# case1 : 음수부 하나와 양수부 하나
# case2 : 양수부 하나와 음수부 하나
# case3 : [0,0,0]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        if len(nums) < 3 or nums[-1] < 0:
            return []
        
        m2p_idx = 0
        answer = []
        ans_set = set()
        
        # minus가 하나 나머지가 plus일 때
        minus_set = set()
        plus_set = set()
        for i, n in enumerate(nums):
            if n >= 0:
                m2p_idx = i
                for n2 in nums[i:]:
                    plus_set.add(n2)
                break
            else:
                minus_set.add(n)

        for i in range(m2p_idx):
            for j in range(i+1, m2p_idx):
                if -(nums[i]+nums[j]) in plus_set and (nums[i],nums[j], -(nums[i]+nums[j])) not in ans_set:
                    answer.append([nums[i],nums[j], -(nums[i]+nums[j])])
                    ans_set.add((nums[i],nums[j], -(nums[i]+nums[j])))
                    
        for i in range(m2p_idx, len(nums)):
            for j in range(i+1, len(nums)):
                if -(nums[i]+nums[j]) in minus_set and (nums[i],nums[j], -(nums[i]+nums[j])) not in ans_set:
                    answer.append([nums[i],nums[j], -(nums[i]+nums[j])])
                    ans_set.add((nums[i],nums[j], -(nums[i]+nums[j])))
        if nums[m2p_idx:m2p_idx+3] != [0,0,0]:
            return answer
        else:
            return answer + [[0,0,0]]
