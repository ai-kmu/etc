# 우선 max(nums)이하의 모든 소수를 구함
# nums를 오른쪽 부터 탐색하며 자신의 오른쪽 숫자보다 큰 수가 나올 시
# 해당 숫자를 감소시켜 줌

class Solution:
    def get_eratosthenes(self, n):
        is_prime = np.ones(n+1, dtype=bool)
        is_prime[:2] = False
        N_max = int(np.sqrt(n))
        for j in range(2, N_max+1):
            is_prime[2*j::j] = False

        return is_prime


    def primeSubOperation(self, nums):
        prime_matrix = self.get_eratosthenes(max(nums)) # 소수를 구함

        for i in range(len(nums[::-1])-2, -1, -1):
            prime_num = 0
            idx = 2
            # 감소시킬 수 있는 숫자 중 가장 작은것부터 탐색함
            while nums[i] - prime_num >= nums[i+1]:
                if idx >= nums[i]:
                    return False
                prime_num = idx * prime_matrix[idx]
                idx += 1
            nums[i] -= prime_num


        return True
        

