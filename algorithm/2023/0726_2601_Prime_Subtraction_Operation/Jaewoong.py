class Solution(object):
    def primeSubOperation(self, nums):
        # 1부터 1000까지 소수 모두 찾는다
        prime_num = [2, 3]
        for i in range(5, 1001):
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                prime_num.append(i)
        # nums 행렬의 값을 뺄 수 있는 만큼 빼줍니다
        for i in range(len(nums)):
            if i == 0:
                idx = bisect.bisect_left(prime_num, nums[i])
                if idx > 0:
                    nums[i] -= prime_num[idx - 1]
            else:
                if nums[i] > nums[i - 1]:
                    idx = bisect.bisect_left(prime_num, nums[i] - nums[i - 1])
                    if idx > 0:
                        nums[i] -= prime_num[idx - 1]
                # 값이 동일하거나 idx보다 작은 값이면 False return
                else:
                    return False
        return True
