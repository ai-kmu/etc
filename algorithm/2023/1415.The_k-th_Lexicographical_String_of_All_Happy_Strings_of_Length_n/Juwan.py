

class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        # a, b, c로만 이루어져있는 문자열
        # 전체 문자열에 대해서 s[i] != s[i + 1]
        # n과 k가 주어졌을 때
        # n개를 가질 수 있는 문자열 중에서 사전식으로 정렬했을 때 k번째 string을 구하라.

        # 사전식 정렬이니까..
        # a -> b -> c 순서로 문자가 구성될 것
        
        cnt = 0 # 만약 cnt가 k번째가 되면 재귀함수를 멈출 거임
        result = '' # cnt가 k가되면 현재 생성된 문자열을 담을 변수

        mapping = { 
            'a' : ['b', 'c'], # a 다음엔 b, c가 올 수 있음
            'b' : ['a', 'c'],
            'c' : ['a', 'b']
        }

        def recur(prev='', cur=''):
            nonlocal cnt
            nonlocal result

            if len(cur) == n: # 만약 생성한 문자열의 길이가 n이면
                cnt += 1 # cnt 증가시키고
                if cnt == k: # k번째 수와 일치하면 result 갱신
                    result = cur
                return

            if cnt > k: # 만약 생성한게 k를 넘어가면 '' 리턴
                return

            for nxt in mapping[prev]: # 위 조건을 만족 못했을 시
                recur(nxt, cur + nxt) # 다음 문자열을 이어붙여서 재귀 탐색

        recur('a', 'a')
        recur('b', 'b')
        recur('c', 'c')
        
        return result

        
