from collections import defaultdict

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:  # trivial case
            return False

        quotient = len(nums) // k
        dic = defaultdict(int)

        for _ in nums:
            dic[_] += 1

        for i in range(quotient):
            element = min(dic)
            for j in range(k):
                if dic[element] == 0:  # 연달아 할 수 없다면 False
                    return False
                dic[element] -= 1  # 썼으면 하나 차감
                if dic[element] == 0:  # 없으면 삭제 
                    del dic[element]
                element += 1  # 연달아 해

        return True
