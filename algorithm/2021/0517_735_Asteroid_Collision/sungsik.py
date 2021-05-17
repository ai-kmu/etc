from collections import deque


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for ast in asteroids:
            # 소행성이 양수이거나 stack이 비어있을 경우 무조건 추가한다.
            if ast > 0 or not stack:
                stack.append(ast)
            # 소행성이 음수이면서 stack이 비어있지 않을 경우
            else:
                # stack이 비어있지 않고, top이 양수이면서 그 값이 충돌하는 소행성의 크기보다 작을 경우
                # 계속 소행성을 stack에서 pop한다.
                while stack and stack[-1] > 0 and stack[-1] < abs(ast):
                    tmp = stack.pop()
                # 만약 top의 소행성과 충돌하는 소행성의 크기가 같을 경우
                # top의 소행성과 충돌하는 소행성 모두 제외시킨다.
                if stack and stack[-1] == abs(ast):
                    stack.pop()
                    continue
                # stack이 비어있거나, top 소행성이 음수일 경우
                # 소행성이 모두 충돌시켜서 파괴시켰거나 충돌한 소행성이 없다고 판단하여
                # stack에 추가한다.
                if not stack or stack[-1] < 0:
                    stack.append(ast)

        return list(stack)