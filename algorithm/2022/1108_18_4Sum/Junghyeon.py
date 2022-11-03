'''
num.length의 최대 길이가 200이므로 O(n^4)으로 시도
중간중간 꼼수를 이용해서 타임아웃 해결
'''
from collections import Counter


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = list()
        
        # nums에 있는 원소의 개수를 구함
        Counter(nums)
        
        tmp_list = list()
        tmp2_list = list()
        
        # nums의 원소마다 최대 개수를 4개로 제한
        for i, j in Counter(nums).items():
            if j > 4:
                tmp_list += [i] * 4
            else:
                tmp_list += [i] * j
        
        nums = tmp_list[:]
        
        nums.sort()
        
        # nums의 길이가 4 미만이면 정답이 없음
        if len(nums) < 4:
            return []
        
        # 배열된 nums에서 맨 앞의 4개의 합이 target보다 크면 정답이 없음
        # 반대의 경우도 맨 뒤의 4개의 합이 target보다 작으면 정답이 없음
        if sum(nums[-4:]) < target or sum(nums[:4]) > target:
            return []
        
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    for w in range(z+1, len(nums)):
                        # 정렬이 되어 있으므로 target값을 넘어가면 break
                        if nums[x] + nums[y] + nums[z] + nums[w] > target:
                            break
                        # 이미 정답을 찾았으므로 break    
                        if nums[x] + nums[y] + nums[z] + nums[w] == target:
                            tmp2_list.append([nums[x], nums[y], nums[z], nums[w]])
                            break
        
        # 중복제거
        for i in tmp2_list:
            if i not in result:
                result.append(i) 
            
        result.sort()
        
        return result
