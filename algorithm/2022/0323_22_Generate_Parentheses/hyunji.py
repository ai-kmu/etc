# parentheses 가 완성되기 전까지 '(' 가 항상 ')' 보다 선행되어 존재해야 하고, 개수도 더 많이 존재해야 한다
# 각각 변수 left, right는 쓸 수 있는 '(' 의 개수, ')' 의 개수를 의미한다
# right 가 0 인 경우가 parentheses 가 완성된 상태

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generateP(left, right, s):
            if left > 0:
                # recursive 방식으로 left의 개수를 하나 줄여주고, s 문자열에 '(' 를 add 해줌
                generateP(left-1, right, s+'(')
                
            # ')' 개수보다 '(' 의 개수가 더 많아야 한다
            if right > left:
                generateP(left, right-1, s+')')
                
            if right == 0:
                res.append(s)
            return res
        
        generateP(n, n, '')
        return res
