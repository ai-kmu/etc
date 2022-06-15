from collections import deque


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # histogram에서 가장 큰 rectangle area를 찾아라
        answer = 0
        
        stack = deque([]) # 단조 증가 stack
        heights.append(0) # 마지막에 끝내기 위한 0 추가
        
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v: # 현재 v보다 클 때까지 뽑아서 area update
                height = heights[stack.pop()] # 뽑은 height
                if stack: # 뽑은 height를 최소로 하는 요소들의 길이 계산
                    length = i - stack[-1] - 1 # 현재부터 stack[-1]이후까지 height를 보장
                else:
                    length = i # stack이 없다면 0번째부터 height를 보장
                answer = max(answer, height * length)
            stack.append(i)
        return answer
