from math import sqrt, floor


class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False

        for i in range(2, floor(sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True


    def primeSubOperation(self, nums: List[int]) -> bool:

        original = nums[:] # 배열의 원본값 보존
        start = 0
        l = len(nums)

        while True:
            # search section
            # start 부터 단조 증가인지 점검
            for i in range(start, l - 1):
                if nums[i] < nums[i + 1]:
                    continue
                else:
                    start = i
                    break
            
            else:  # loop finished normally -> nums is strictly increasing array
                return True
                
            # operation section
            # 단조 증가 조건을 만족하는 (original[start] - p) 를 찾음
            p = original[start] - nums[start] + 1
            while p < original[start]:
                cand = original[start] - p
                if self.isPrime(p) is True and cand < nums[start + 1]:
                    nums[start] = cand
                    break
                else:
                    p += 1

            else:  # loop finished normally -> this case is impossible
                return False
                    
            # validation section
            # nums[start]가 바뀌어서 오름차순 조건이 깨졌다면, 전으로 돌아가서 수정
            if start >= 1 and nums[start - 1] >= nums[start]:
                start -= 1
