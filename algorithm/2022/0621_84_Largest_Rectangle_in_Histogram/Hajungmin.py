class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack, 정답, 양옆으로 0을 더해준 heights를 선언
        # 뒤에 0을 더해주는 이유 -> [2, 4] 이런 예제의 경우
        # [0, 2, 4, 0]으로 계산해야 값이 정확히 계산되기 때문에
        # 반면 [2,1,5,6,2,3]의 경우는 뒤에 0이 없어도 된다.
        stack = []
        max_area = 0
        heights = [0] heights + [0]
        
        # heights를 돌며 index를 스택에 넣어줌
        for idx, item in enumerate(heights):
            if len(stack) > 0:
                # 만약 스택이 비어있지 않고
                # 다음 값이 현재 값보다 작다면 루프를 돔
                while item < heights[stack[-1]]:
                    top = stack.pop()
                    # 스택에서 가장 위의 인덱스를 뽑아 영역을 계산
                    max_area = max(max_area, heights[top] * (idx - stack[-1] - 1))
            # 다음 값이 현재 값보다 클 때는 계속 append해줌
            stack.append(idx)
        return max_area
