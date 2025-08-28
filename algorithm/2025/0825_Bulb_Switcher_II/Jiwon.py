class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        if presses == 0:
            return 1
        
        # 버튼 1: 1 / 버튼 2, 3: 2 / 버튼 3: 3 -> 6까지만 보면 됨
        n = min(n, 6)
        res = set()
            
        def press(state, btn):
            if btn == 0:
                return [not x for x in state]
            elif btn == 1: 
                return [not x if (i+1) % 2 == 0 else x for i, x in enumerate(state)]
            elif btn == 2: 
                return [not x if (i+1) % 2 == 1 else x for i, x in enumerate(state)]
            elif btn == 3:
                return [not x if (i % 3 == 0) else x for i, x in enumerate(state)]

        # 버튼 4개에 대해 짝수번/홀수번만 고려하면 됨
        for button_press in product([0, 1], repeat = 4):
            cnt = sum(button_press)
          
            # 짝홀수 및 유효범위 검사 
            if cnt % 2 == presses % 2 and cnt <= presses:
                bulb = [True for i in range(n)]
                for i in range(4):
                    if button_press[i]:
                        bulb = press(bulb, i)
                res.add(tuple(bulb))

        return len(res)
