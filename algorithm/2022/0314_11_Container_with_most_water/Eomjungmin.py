class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Two pointer 방법으로 접근
        start = 0 # 시작점
        end = len(height)-1 # 끝점
        water_max = 0 # 최대 area 저장
        
        # 시작점과 끝점에서의 길이와 밑변을 이용하여 area를 구함
        # 구한 area와 최신 max_area 중 비교하여 큰것을 area로 갱신
        # area가 최대로 나오게 하기 위해 시작점과 끝점의 height를 비교
        # end에서 더 크면 start를 1 증가시키고
        # 아니면 끝점을 1 감소시킴
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            water_max = max(water_max, area)
            
            if height[start] < height[end]:
                start+=1
            else:
                end-=1
            
        return water_max # 최종 max area 출력
