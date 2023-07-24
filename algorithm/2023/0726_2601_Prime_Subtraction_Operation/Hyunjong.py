class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # 소수 배열 생성
        prime = [True] * 1001
        prime[0] = prime[1] = False
        for x in range(2, 1001):
            if prime[x]:
                # 소수의 배수들을 제외하여 소수 체크
                for i in range(x * x, 1001, x):
                    prime[i] = False

        prev = 0
        for x in nums:
            if prev >= x:
                # 이전 값보다 현재 값이 작거나 같으면 False 반환
                return False

            for p in range(x - 1, -1, -1):
                # 현재 값 x와 합으로 표현될 수 있는 소수 p를 찾음
                if prime[p] and x - p > prev:
                    break

            prev = x - p

        return True
