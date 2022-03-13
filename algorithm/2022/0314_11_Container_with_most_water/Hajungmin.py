class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 시작 지점, 끝 지점, 현재까지 저장 가능한 물을 선언
        start_point = 0
        end_point = len(height) - 1
        water = 0
        
        # 시작 지점이 끝 지점보다 커지는 시점까지 루프를 돈다
        while start_point < end_point:
            # 저장 가능한 물은 현재 시점 height 값과 끝 지점 height 값 사이에 작은 값 * 사이 거리를 통해 구한다.
            # 이후 현재 저장 가능한 물의 용량과 비교해서 더 큰 값으로 업데이트 한다.
            water = max(water, min(height[start_point], height[end_point]) * (end_point - start_point))
            
            # 만약 현재 지점의 height 값 보다 끝 지점 height 값이 더 크면 시작 지점을 한 칸 더한다
            if height[start_point] < height[end_point]:
                start_point += 1
            
            # 현재 지점의 height 값 보다 끝 지점 height 값이 더 작으면 끝 지점을 한 칸 감소시킨다
            else:
                end_point -= 1
                
        return water
