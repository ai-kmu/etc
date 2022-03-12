class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        start = 0
        end = len(height) - 1

        #start,end를 사용해서 양쪽 끝에서부터 최대 길이를 사용해서 점점 줄여나감
        #양쪽의 숫자중에서 작은 숫자를 길이와 곱해줌
        #양쪽의 숫자중에서 작은 숫자가 곱해지기 때문에 작은 숫자의 포인터를 옮김
        #모든 과정에서 max값을 사용하여 최대값을 갱신
        #최대 길이부터 사용하고 양쪽의 숫자 중에서 작은 숫자를 바꾸기 때문에 그 과정에서 가질 수 있는 최대값을 가질 수 있겠다고 생각했음
        while start < end:
            if height[start] <= height[end]:
                answer = max(answer,height[start]*(end-start))
                start += 1
            else:
                answer = max(answer,height[end]*(end-start))
                end -= 1
        return answer
