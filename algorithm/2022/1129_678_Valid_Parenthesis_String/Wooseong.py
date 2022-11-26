# 왜 안 되는지 모르겠는 첫 시도
'''
일반적인 valid parenthesis 문제처럼
queue에다가 '('를 넣고 ')'가 나올 때마다 pop하도록 했다
근데 queue가 없을 때는 '*'를 '('로 쓸 수 있으니까
'*'의 개수를 insurance로 세두었다

for문을 다 돌고 난 뒤,
queue에 '('가 남아 있으면 '*'을 ')'로 써서 다 닫도록 했다
이떄 '('보다 '*'이
	적으면      == invalid
	많거나 같으면 == valid
따라서 insurance >= 0일 경우 True, 아닐 경우 False처리
'''
from collections import deque

class Solution:
    def checkValidString(self, string: str) -> bool:
		# '('를 넣어둘 q와 '*'의 개수를 셀 insurance
        q = deque([])
        insurance = 0
		
		# 쭉 돌면서
        for s in string:
			# '('는 넣고
            if s == "(":
                q.append(s)
			# ')'가 나오면
            elif s == ")":
				# '('가 있으면 빼고
                if q:
                    q.pop()
				# 없을 때
                elif not q:
					# '*'이 있으면 걜 빼고
                    if insurance > 0:
                        insurance -= 1
					# 걔도 없으면 False
                    else:
                        return False
			# '*'가 나오면 세기
            elif s == "*":
                insurance += 1
        
		# 다 돌고 남은 '('를 '*'로 제거
        while q:
            q.pop()
            insurance -= 1
        
		# '('가 더 많이 남았으면 insurance < 0 됨 == False
        return True if insurance >= 0 else False

# 다른 알고리즘으로 바꿈
'''
Valid 하려면 '('와 ')'의 개수가 같아야 됨
근데 '*'가 '(', ')', 심지어 ''로도 쓰임
-> ')'는 '('를 하나 줄이는 애로 삼으면
   '*'는 '('를 하나 줄이거나 늘리는 애가 됨
   -> '(' 개수의 범위가 생김
'''
from collections import deque

class Solution:
    def checkValidString(self, string: str) -> bool:
		# 가능한 '(' 개수의 최소, 최댓값
        min_ = 0
        max_ = 0
		
		# 쭉 돌면서
        for s in string:
			# '('가 나오면 최소 최대 둘 다 늘림
            if s == "(":
                min_ += 1
                max_ += 1
			# ')'가 나오면 최소 최대 둘 다 줄임
            elif s == ")":
                min_ -= 1
                max_ -= 1
			# '*'을 ')'로 쓸 경우 최소가 하나 줄고
			# '*'을 '('로 쓸 경우 최대가 하나 늘어남
            elif s == "*":
                min_ -= 1
                max_ += 1
			
			# '*'을 ')'로 써서 최소를 줄이되, -1까지 줄일 순 없음
            min_ = max(min_, 0)
            
			# 최대가 0보다 작다 == 가능한 '('의 개수보다 현재 ')'의 개수가 많다
			# == invalid
            if max_ < 0:
                return False
        
		# valid == '('를 다 썼다 -> 최소 == 0
        return min_ == 0
