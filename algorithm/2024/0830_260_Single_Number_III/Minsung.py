class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        counter = defaultdict(int)
        ans = list()
        
        # 각 value가 몇 번 등장했는지 count
        for i in nums:
            counter[i] += 1

        # 한 번만 등장한 value -> answer
        for k, v in counter.items():
            if v == 1:
                ans.append(k)
        return ans
