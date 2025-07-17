class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        answer = []

        def rec(index, sub):
            if sub and sum(sub) == n:
                if(len(sub) == k):
                    answer.append(sub)
                return
            
            if (index >= len(nums)):
                return
            
            rec(index + 1, sub + [nums[index]])

            rec(index + 1, sub)

        rec(0,[])

        return answer
