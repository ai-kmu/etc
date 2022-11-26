class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # dp는 왼쪽 괄호 개수에서 오른쪽 괄호 개수를 뺀 수의 경우의 수를 모두 저장
        dp = [set([0]) for _ in range(n+1)]
        
        add = lambda x: x+1
        sub = lambda x: x-1

        for i in range(1, n+1):
            # 왼쪽 괄호일 경우 이전 모든 경우의 수에서 1을 더함
            if s[i-1] == '(':
                dp[i] = map(add, dp[i-1])
            # 왼쪽 괄호일 경우 이전 모든 경우의 수에서 1을 뺌
            elif s[i-1] == ')':
                dp[i] = map(sub, dp[i-1])
            # *일 경우 3가지를 모두 구해 경우의 수를 합침
            else:
                add_tmp = map(add, dp[i-1])
                sub_tmp = map(sub, dp[i-1])
                dp[i] = dp[i-1].union(add_tmp).union(sub_tmp)
            # 음수의 경우 올바르지 못한 경우의 수이므로 제거
            dp[i] = set([x for x in list(dp[i]) if x >= 0])
            # 만약 모두 음수일 경우 return False
            if not dp[i]:
                return False
        
        # 모든 괄호를 읽고 경우의 수 중 0이 있을 경우 return True
        return 0 in dp[-1]
