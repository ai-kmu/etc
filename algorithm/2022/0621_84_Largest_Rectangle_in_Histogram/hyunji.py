# 오답코드..
# 중간 test case 에서 오류 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        answer = 0
        stack = []
        
        for i in range(len(heights)):
            
            # 현재 heigth가 직전에 stack으로 들어온 height 값보다 작을 때
            while stack and heights[i] <= stack[-1][0]:
                u, t = stack.pop()
                
                # 만약 stack이 비어있다면 현재 height * index 와 answer 비교
                if not stack:
                    answer = max(answer, u * t)
                
                # 만약 stack에 값이 존재하면 
                # '현재 index와 저장된 stack값의 index 간의 거리차 - 1' 가 밑변 길이
                else:
                    answer = max(answer, u * (i - stack[-1][-1] -1))
                
            stack.append((heights[i], i))
                
        return answer
                
        
