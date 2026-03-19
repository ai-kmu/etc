import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 하키스틱 문제와 비슷?
        # matrix index를 조합으로 치환해보면 (m>n 기준)
        # m은 m에서 n만큼 벌어지고(대각선 기준으로 같으니), n에서는 0만큼 벌어짐.
        # 예시 : 7, 3의 경우 7C3은 7C0에서 3칸 멀어짐. 조합 계산은 행렬의 크기 - 1만큼 계산됨. 0C0부터 시작해야하니 (zero index)
        # 따라서 6C2로 계산해야함.
        # 수식화하면 (m-1)+(n-1)C(n-1) if m > n
        return math.comb(m+n-2,min(m,n)-1)
