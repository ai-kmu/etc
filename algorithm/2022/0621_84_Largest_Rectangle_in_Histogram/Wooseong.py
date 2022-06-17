# 직사각형 만드는 방법
# 1. 자신의 높이를 그대로 갖고 오른쪽으로 확장
#    - 뒤에가 자기보다 낮을 때 stop
# 2. 자신보다 낮은 높이를 갖고 오른쪽으로 확장
#    - 위치에 따른 가능 높이를 갱신


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0
        stack = []
        n = len(heights)
        
        for i, h in enumerate(heights):
            left = i
            # 1번 방법: stack[-1][1] = 자신의 높이 / h = 뒤의 높이
            while stack and stack[-1][1] > h:
                # ind   : "자신"의 위치
                # height: "자신"의 높이
                # i     : "뒤"의 위치
                # 따라서 가로는 i - ind
                ind, height = stack.pop()
                answer = max(answer, height * (i - ind))
                left = ind
            
            stack.append((left, h))
        
        # 2번 방법
        # stack[i][0]: 자신의 위치
        # stack[i][1]: 자신 포함 오른쪽에서의 최솟값
        # 따라서 가로는 n - stack[i][0]
        temp = max([pair[1] * (n - pair[0]) for pair in stack])
        answer = max(answer, temp)
        
        return answer
