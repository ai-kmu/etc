class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        "(" 보다 ")"가 많이 올 수 없다.
        처음에 "("를 넣고 "("와 ")"를 넣으면서 조건에 맞는 스트링을 저장
        "("과 ")"의 최대 개수를 각각 n으로 설정 
        '''
        result = list()
        
        def recur(s, l, r):
            # l과 r이 모두 0일때 result에 추가해서 리턴
            if l == 0 and r == 0:
                return result.append(s)
            if l > 0:
                recur(s+'(', l-1, r)
            if r > l:
                recur(s+')', l, r-1)
        # 항상 "("으로 시작을 하기 때문에 s에 기본값으로 "("를 넣어준다.
        # 이미 "("가 한개 있기 때문에 l에는 n-1을 넣어주고 r에는 n을 넣어서 recur를 호출한다.
        recur('(', n-1, n)
        
        return result
