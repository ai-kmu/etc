class Solution:
    def kthGrammar(self, n, k):
        # 기본 경우: n이 0 또는 1일 때, 트리에는 값이 0인 단일 노드만 존재.
        if n == 1 or n == 0:
            return 0
        
        # 현재 레벨의 문자열 길이를 계산 (2^(n-1)).
        length = 1 << (n - 1)
        
        # 현재 레벨의 중간 위치를 계산
        mid = length // 2
        
        # 원하는 위치 k가 현재 레벨의 중간 위치 이하인 경우,
        # 이전 레벨 (n-1)과 동일한 위치 (k)에 대해 재귀적으로 함수를 호출.
        if k <= mid:
            return self.kthGrammar(n - 1, k)
        else:
            return int(not self.kthGrammar(n - 1, k - mid))

