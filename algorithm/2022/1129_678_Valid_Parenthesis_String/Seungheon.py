class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # '('의 step_size 는 +1
        # ')'의 step_size 는 -1 이라고 할때 string의 마지막에서는 step의 합이 0이 되어야 한다.
        # -> '('일때는 이전 step에서 1을 더해주고, '('일때는 이setp에서 1을 빼준다.
        # -> '*'일때는 1을 더해주거나 1을 빼주거나 이전 step을 그대로 가져간다.
        # step을 저장할때 중복을 제거하기위해 set을 사용한다.
        # string의 마지막에 도달했을때 0을 포함하고 있으면 True 아니면 False를 반환한다

        steps = set([0])
        for idx, ch in enumerate(s):
            next_steps = set()
            for step in steps:
                if step <0:
                    continue
                if ch == '(':
                    next_steps.add(step+1)
                elif ch == ')':
                    next_steps.add(step-1)
                else: # *인경우
                    next_steps.add(step+1)
                    next_steps.add(step-1)
                    next_steps.add(step)
            steps = next_steps

        return True if 0 in steps else False
