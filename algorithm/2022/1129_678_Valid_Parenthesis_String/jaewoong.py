class Solution:
    # 투스택 솔루션
    def checkValidString(self, s: str) -> bool:
        stack, star = [], []
        # 인덱스: 단어위치
        # (의 끝에는 *나 )가 있어야됨
        # (가 나오고 우선 ) 만 먼저 처리
        # *은 만능으로 (뒤에 *만 남아있거나
        # * 뒤에 ) 만 남아있으면 되는데
            # 단, (뒤에 *이 있고 )가 없는 경우
            # *이 (보다 많거나 같아야 되고 '[(,(,*]'
            # (이 없고 *랑 )만 있는 경우
            # *가 )보다 많거나 같아야한다. '[*,),)]인 경우 실패'
            
        for i,char in enumerate(s):
            if char == "(": stack.append(i)
            elif char == ")":
                if not stack and not star: return False
                elif stack: stack.pop()
                elif star: star.pop()
            else: star.append(i)
    
        while stack:
            # '*, *, (' 인 경우에 대한 예외
            if star and stack[-1] < star[-1]:
                stack.pop()
                star.pop()
            else:
                if not star: return False
                else: star.pop()
		
        return True
