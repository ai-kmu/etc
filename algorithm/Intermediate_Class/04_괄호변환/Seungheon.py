from collections import deque
import copy
def solution(p):
    
    # 2 균형잡힌 문자열 u, v로 분리
    def separation(p):
        u = deque()
        stack = []
        poped = p.popleft()
        stack.append(poped)
        u.append(poped)
        # 스택이 비면 균형잡힌 문자열이 만들어 진것
        while stack:
            poped = p.popleft()
            u.append(poped)
            if stack[-1] == poped:
                stack.append(poped)
            else:  
                stack.pop()
        return u, p
    
    
    # 3 u가 올바른 문자열인지 확인
    def check_correct(origin_u):
        u = copy.deepcopy(origin_u)
        # u_stack안에는 '('만 저장된다
        u_stack = []
        while u:
            poped = u.popleft()
            # 뽑힌것이 '('이면
            if poped == '(':
                u_stack.append(poped)
            # 뽑힌것이 ')'이면
            else:
                # u_stack 이 비었으면
                if not u_stack:
                    return False
                else:
                    u_stack.pop()
        return True
    
    p = deque(p)
    def transform(p=p):

        # 1
        if not p:
            return ''
        
        # 2 균형잡힌 문자열 u, v로 분리
        u, v = separation(p)

        # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        if check_correct(u):
            u.extend(transform(v))
            return u
        
        else:
            # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            answer = ['(']

            # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            answer.extend(transform(v))
 
            # 4-3. ')'를 다시 붙입니다. 
            answer.append(')')
            
            # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            u.popleft()
            u.pop()
            u = list(map(lambda x : ')' if x == '(' else '(' ,u))
            answer.extend(u)
            
            # 4-5. 생성된 문자열을 반환합니다.
            return answer

    return ''.join(transform(p))
