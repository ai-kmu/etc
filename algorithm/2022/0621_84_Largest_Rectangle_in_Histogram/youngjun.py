#Solution 1: brutal force 이용하여 풀이, Time limit 걸림

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #max_area를 0으로 초기화한다.
        max_area = 0
        
        #히스토그램에서 인덱스 i부터 j사이의 최소 높이와 너비의 최댓값을 구하는 문제이므로, 이중 for문을 사용한다. 
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                #높이 최솟값의 기준은 j가 변화할때마다 inf로 초기화한다.
                min_height = inf
                j가 변화할 때, i부터 j까지의 범위 사이의 높이 최솟값을 구한다.
                for hi in range(i,j+1):
                    min_height = min(min_height,heights[hi])
                #위에서 구한 min_height에 (j-i+1)을 하게 될 경우 해당 범위의 넓이를 구할 수 있으므로, 최댓값을 갱신한다.
                max_area = max(max_area,min_height*(j-i+1))
                
        return max_area

#Solution 2: stack 이용하여 풀이, Testcase 걸림

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []

        for i,h in enumerate(heights):
            
            while stack and stack[-1][1] > h:
                min_index, min_height = stack.pop()
                max_area = max(max_area,min_height*(i-min_index))
                
            stack.append([i,h])
            
        return max_area
