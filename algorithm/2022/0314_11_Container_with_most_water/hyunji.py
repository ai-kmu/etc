'''
height 배열을 순서대로 완전탐색하면 Time Limit Exceeded가 걸림
--> 그래서 맨 처음과 맨 뒤 두 개의 기준점을 두고 양방향으로 height 배열을 탐색해주었다

1. 두 개의 기준점 l, r을 height 배열의 index로 주어주고, height[l], height[r] 중 더 작은 것을 container의 세로 길이로 배당해준다. 
2. 정해진 세로 길이를 가로 길이 (r-l)과 곱해주고, 이것이 기존의 maxarea 보다 넓이가 더 크면 새롭게 maxarea를 할당해준다.
3. height[l]과 height[r] 중에서 값이 더 작은 것의 index를 찾아서, 그것이 l일 경우 1만큼 증가, r일 경우 1만큼 감소시켜준다.
4. 이렇게 l이 r보다 크거나 같아지는 경우 while문을 종료시킨다. 
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l = 0 
        r = len(height)-1
        
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r])*(r-l))
        
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxarea
