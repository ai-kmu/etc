class Solution:
    def is_prime(self, num): 
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def primeSubOperation(self, nums: List[int]) -> bool:
        max_reach = nums[0]
        for i in range(1, len(nums)):
            num = nums[i] # 현재 값이 최대 도달 가능한 값보다 작거나 같다면 배열증가 불가능
            if num <= max_reach:
                return False
            found = False # num 미만의 소수들을 찾아서 뺄셈하여 배열 업데이트
            for p in range(num - 1, 1, -1):
                if self.is_prime(p) and p < num:
                    nums[i] -= p
                    found = True
                    break 
            if not found:
                return False  # 최대 도달 가능한 값 업데이트
            max_reach = max(max_reach, nums[i]) # 모든 원소를 엄격히 증가시키는 것이 가능
        return True
