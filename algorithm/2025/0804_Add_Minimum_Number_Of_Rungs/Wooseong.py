class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        ans = 0  # 누적합을 위한 사전 할당

        left = 0  # 현재 height = 0
        for num in rungs:
            cur_dist = num - left  # 다음 칸까지의 거리 확인
            left = num  # 현재 위치 변경

            # dist보다 거리가 작거나 같으면 넘어감
            if cur_dist <= dist:
                continue
            
            # dist보다 크면 다음과 같은 개수의 ladder가 추가로 필요함
            ladder = (cur_dist - 1) // dist
            ans += ladder
        
        return ans
        
