class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prime = [True]*1001  # idx 가 소수인지 아닌지 나타내는 배열
        prime[0] = prime[1] = False  # 0, 1은 무조건 소수가 아니므로 false

        for x in range(2,1001):
            if prime[x]:  # 만약 소수이면
                for i in range(x*x, 1001, x):  # 그 수의 배수들은 소수가 아니므로
                    prime[i] = False

        prev=0
        for x in nums:
            if prev >= x:  # 이전 값이 다음 값보다 크면 오름차순이 아니므로 
                return False  # 바로 false return

            for p in range(x-1, -1, -1):  # x보다 작은 약수중에 가장 큰 약수를 골라야 하므로 
                if prime[p] and x-p > prev:  # p가 약수이고 x-p가 오름차순을 유지한다면
                    break

            prev=x-p

        return True    
