# 풀이실패..
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        nums.sort() #1,2,3,5
        cost.sort()
        # 리스트를 여러개 만들어서 비교해볼 예정
        for i in range(len(nums)):
            ans+'i' = []
        #cost 1,2,3,14
        res = 0
        
        for c in range(len(cost)):
            for n in range(len(nums)):
                res = c + n
                # 값이 같은게 있으면 해당 리스트에 값을 추가
                if res == nums[c]:
                    ans.append(res)

        return ans
                    
