'''
패턴을 보면

0
0110
0110 1001
0110 1001 1001 0110
0110 1001 1001 0110 1001 0110 0110 1001
0110 1001 1001 0110 1001 0110 0110 1001 1001 0110 0110 1001 0110 1001 1001 0110

A
AB
ABBA
ABBA BAAB
ABBA BAAB BAAB ABBA
-> 기존 거에 기존 걸 반전 시킨 걸 붙이는 거임

다시 그려보면
         A
       A   B
  A    B   B    A
 AB   BA   BA   AB
ABBA BAAB BAAB ABBA

그니까 절반 앞부분은 그대로 가고, 뒷부분은 반전이 되는 걸 알 수 있음
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n, k, val):
            if n == 1:
                return val
            
            num_nodes = 2 ** (n - 1)
            # 뒤는 반전
            if k > (num_nodes / 2):
                next_ = 1 - val
                return dfs(n - 1, k - (num_nodes / 2), next_)
            # 앞은 그대로
            else:
                next_ = val
                return dfs(n - 1, k, next_)

        return dfs(n, k, 0)
