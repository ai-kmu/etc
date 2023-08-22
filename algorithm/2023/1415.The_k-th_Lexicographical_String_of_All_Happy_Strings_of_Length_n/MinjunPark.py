class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        s = ['a', 'b', 'c']
        answer = []


        def makeHappyString(n, hs):
            if n == 0:  # happystring을 answer에 append
                answer.append(hs)
                return
            
            for i in s:
                if i == hs[-1]:  # unhappystring이 될 경우에 진행하지 않음
                    continue

                makeHappyString(n - 1, hs + i)  # dfs로 생성


        for i in s:  # 최초 문자열 'a', 'b', 'c'
            makeHappyString(n - 1, i)

        if k > len(answer):
            return ''
        else:
            return answer[k-1]  # answer은 이미 사전 순으로 정렬되어 있음
