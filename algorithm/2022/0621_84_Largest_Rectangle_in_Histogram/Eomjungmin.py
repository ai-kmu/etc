class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # stack 선언. stack에는 (인덱스, 넓이) 형식으로 저장
        max_a = 0 # 최대 넓이 갱신을 위한 변수 선언
        heights.append(0)
        
        for i in range(len(heights)): # height 루프
            ind = i
            # stack 마지막 저장 튜플의 넓이 값이 현재 height보다 크거나 같으면 아래 루프 반복
            while stack and stack[-1][1] >= heights[i]: 
                # 가장 최근 stack의 인덱스와 그 넓이 뽑기
                ind, area = stack.pop()
                # 가로 폭 계산 후 최대 넓이 갱신
                width = i - ind
                max_a = max(max_a, area * width)
            # stack에 인덱스와 넓이 저장
            stack.append((ind, heights[i]))
            
        # stack에 있는 (인덱스, 넓이)를 이용해서 최대 넓이 갱신
        for ind, bar in stack:
            max_a = max(max_a, bar * (len(heights)-i))
            
        return max_a
