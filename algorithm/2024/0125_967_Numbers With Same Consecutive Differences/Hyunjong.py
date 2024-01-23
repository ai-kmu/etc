class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        def dfs(n, index, k):
            # 길이가 0이 되면 가능한 것이니 결과에 추가
            if n == 0:
                result.append(index)

            # 길이가 0보다 크면 숫자를 계속 생성
            else:
                # 현재 숫자의 일의 자리에서 k를 뺀 값이 0 이상이면 재귀 호출
                if (index % 10) - k >= 0:
                    dfs(n - 1, index * 10 + (index % 10) - k, k)
                
                # k가 0이 아니고, 현재 숫자의 일의 자리에서 k를 더한 값이 9 이하이면 재귀 호출
                if k != 0 and (index % 10) + k <= 9:
                    dfs(n - 1, index * 10 + (index % 10) + k, k)
        
        # 1부터 9까지의 숫자로 시작하여 dfs 호출
        for i in range(1, 10):
            dfs(n - 1, i, k)
        return result
