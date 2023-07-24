class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        # n = 1인 경우 항상 참
        if n == 1:
            return True

        # 에라토스테네스의 체
        prime = [False, False] + [True] * 999
        for i in range(2, int(math.sqrt(1000)) + 1):
            if prime[i] == True:
                j = 2
                while i * j <= 1000:
                    prime[i * j] = False
                    j += 1

        # i = 0인 경우에 대해 nums[i]보다 작은 최대 소수를 빼줌
        for i in range(nums[0] - 1, 1, -1):
            if prime[i] == True:
                nums[0] = nums[0] - i
                # i = 0인 경우 strictly increasing인지 확인
                if nums[1] <= nums[0]:
                    return False
                break

        # i = 0인 경우를 제외한 나머지 nums 순회
        for i, v in enumerate(nums):
            if i == 0:
                continue
            # strictly increasing인지 확인
            if v <= nums[i - 1]:
                return False
            # nums[i]에 해당 위치의 숫자보다 작으면서 뺐을 때 전의 숫자보다 큰 경우로 가장 큰 소수를 빼줌
            for j in range(v - 1, 1, -1):
                if prime[j] == True and (v - j) > nums[i - 1]:
                    nums[i] = v - j
                    break

        # 모든 경우를 통과하면 True
        return True
