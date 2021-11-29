class Solution:
    
    def numDistinct(self, s: str, t: str) -> int:
        
        # 동적 프로그래밍.
        dp = [0] * (len(t) + 1) # 두 번째 문장의 길이보다 1만큼 큰 dp 배열 생성
        
        dp[0] = 1 # 맨 처음 원소를 1로 둠.
        d = defaultdict(list) # default 딕셔너리 생성
        for i in range(len(t) - 1, -1, -1):
            
            d[t[i]].append(i + 1) # 각 단어의 위치를 딕셔너리에 저장
        
        # 첫번째 케이스를 예시로 딕셔너리는 defaultdict(<class 'list'>, {'t': [6], 'i': [5], 'b': [4, 3], 'a': [2], 'r': [1]}) 처럼 생성됨.
            
        for c in s: # 첫번째 문장에 대해 loop를 돌면서
            for i in d[c]: # c는 첫번째 문장의 문자하나인데, 이것을 딕셔너리에서 찾는다.
                dp[i] += dp[i - 1]
        return dp[-1]
