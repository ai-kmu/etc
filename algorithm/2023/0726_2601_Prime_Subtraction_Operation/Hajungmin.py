class Solution:
    # 소수를 검사
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # 입력 숫자보다 작은 가장 큰 소수 구하는 함수
    def max_prime(self, num):
        for i in range(num, 0, -1):
            if self.is_prime(i):
                return i
        return 0

    def primeSubOperation(self, nums: List[int]) -> bool:
        # 제일 처음 0을 더해줌
        nums = [0] + nums

        for i in range(1, len(nums)):
            # 루프를 돌며 nums의 이전 값과 현재 값을 뺀 수보다 작은 수 중 가장 큰 소수 구함
            sub = nums[i] - nums[i-1] - 1
            sub_prime = self.max_prime(sub)
            
            # 구해진 수를 현재 nums의 값에서 빼서 nums 현재 인덱스 업데이트
            nums[i] = nums[i] - sub_prime

            # 만약 nums의 이전 값이 현재 값보다 크거나 같으면 False
            if nums[i-1] >= nums[i]:
                return False

        # 모두 검사했을 때, 무사히 통과하면 True
        return True

