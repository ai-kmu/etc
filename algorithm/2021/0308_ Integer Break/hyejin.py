class Solution:
    def saperate_k(self, n, num_of_k):
        product = 1
        for i in range(num_of_k):
            k = n//num_of_k
            product *= k
            num_of_k -= 1
            n -= k
        return product
    
    
    def integerBreak(self, n: int) -> int:
        # product의 합이 최대가 되는 수는 중간 수들을 곱한 것.
        # k개로 나누었을 때, k개의 수들이 최소한의 차이가 나는 수로 구성이 되어야함.
        # 2개부터 n-1개까지 그 수를 조사.
        
        answer = 0
        if n == 2:
            return 1
        
        for i in range(2,n):
            answer = max(self.saperate_k(n, i), answer)
        
        return answer
