class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        
        # 에라토스테네스의 체

        if len(nums) == 1:
            return True

        def find_primes(N):
            eratos = [True] * N
            eratos[0], eratos[1] = False, False

            for i in range(2, N):
                if eratos[i] == 1:
                    for j in range(i * 2, N, i):
                        eratos[j] = False

            return eratos

        max_num = max(nums)
        primes = find_primes(max_num) # 에라토스테네스의 체로 소수를 찾음

        prev = 0 # 가장 초기 값
        
        for i in nums:

            if prev >= i: # 만약 i보다 이전 값이 더 크다면 오름차순이 될 수 없음
                return False

            for p in range(i-1, -1, -1): # 숫자 i에서 하나씩 감소시키면서, i보다 작은 소수 중 가장 큰 소수를 찾음
                if primes[p] and i - p > prev: # 만약 그 소수를 i에서 뺏을 때, prev보다 크다면, 오름차순으로 i까지 정렬되었다는 것
                    break # 그럼 break로 멈추고

            prev = i - p # prev를 업데이트 시켜줌

        return True
