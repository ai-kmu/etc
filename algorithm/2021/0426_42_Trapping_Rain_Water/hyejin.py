class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        answer = 0
        curr_max = height[0]
        curr_trapped = []
        for i in range(1, len(height)):
            if len(curr_trapped) == 0 and curr_max < height[i]:
                curr_max = height[i]
                continue

            if len(curr_trapped) != 0 and curr_trapped[-1] < height[i]:
                if curr_max <= height[i]: # 현재 max보다 클 때 list 정리
                    for h in curr_trapped:
                        answer += curr_max - h
                    curr_trapped = []
                    curr_max = height[i]
                else: # 현재 max보다 작지만 list에 있는 것보다 클 때, height[i]만큼 water를 채워주고 answer을 업데이트
                    for j in range(len(curr_trapped)):
                        if curr_trapped[j] < height[i]:
                            answer += height[i] - curr_trapped[j]
                            curr_trapped[j] += height[i] - curr_trapped[j]
                    curr_trapped.append(height[i])
                    
            elif curr_max > height[i]:
                curr_trapped.append(height[i])

        return answer
