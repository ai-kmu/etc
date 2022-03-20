class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursion을 활용한 풀이
        # tmp_s: 지금까지 작성한 괄호식
        # l_flag: tmp_s에서 왼쪽 괄호를 사용한 횟수
        # r_flag: tmp_s에서 오른쪽 괄호를 사용한 횟수
        def recursion(tmp_s, l_flag, r_flag):
            # 현재 길이가 목표한 길이에 도달할 경우
            # tmp_s를 담은 list를 출력
            if len(tmp_s) >= 2*n:
                return [tmp_s]
            # 목표 길이에 도달하지 못했을 경우
            else:
                # 1. 왼쪽 괄호를 n개 사용하지 않았을 경우 왼쪽 괄호를 사용한 케이스를 구함
                left = recursion(tmp_s+'(', l_flag+1, r_flag) if l_flag < n else []
                # 2. 오른쪽 괄호를 왼쪽 괄호만큼 사용하지 않았을 경우 오른쪽 괄호를 사용한 케이스를 구함
                right = recursion(tmp_s+')', l_flag, r_flag+1) if r_flag < l_flag else []
                return left + right
        
        return recursion("", 0, 0)
                
