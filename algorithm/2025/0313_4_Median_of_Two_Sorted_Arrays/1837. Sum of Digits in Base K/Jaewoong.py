class Solution:
    def sumBase(self, n: int, k: int) -> int:
        # 34 = 1*n1 + 6*n2 + 36*n3
        ans_list = []
        for d in range(k):
            for c in range(k):
                for b in range(k):
                    for a in range(k):
                        for i in range(k):
                            for j in range(k):
                                for x in range(k):
                                    if (1*x + k*j + k*k*i + k*k*k*a + k*k*k*k*b +k*k*k*k*k*c+k*k*k*k*k*k*d) == n:
                                        
                                        return x + j + i + a + b + c + d
                                        
