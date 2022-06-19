# test는 통과
# submit 실패
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        max_area = 0
        len_heights = len(heights)
        # 변수 초기화
        for i in range(len_heights):
            x_point = i
            while stack and heights[i] < stack[-1][1]:
                # heights에 대해 stack에 있는 값이 더 큰 경우 stack에 있는 값 뽑아서 계산
                x, h = stack.pop()
                area = h * (i - x)
                max_area = max(max_area, area)
                x_point = x
            stack.append((x_point, heights[i]))
        return max_area
