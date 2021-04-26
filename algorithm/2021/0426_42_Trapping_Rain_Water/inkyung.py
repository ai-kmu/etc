class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: 
            return 0
        
        answer = 0
        # 고점과 고점의 인덱스를 찾고
        highest = max(height)
        idx = height.index(highest)
        
        # 왼쪽부터 가장 고점까지 진행하면서 start기준을 찾고 그거보다 작으면 모두 더해주기
        start = height[0]
        for j in range(idx):
            if height[j] < start:
                answer += start-height[j]
            elif height[j] > start:
                start = height[j]
                
        # 고점을 새로운 시작으로 보고 이후를 진행
        end = height[len(height)-1]
        for k in range(len(height)-1, idx, -1):
            if height[k] < end:
                answer += end - height[k]
            elif height[k] > end:
                end = height[k]
        return answer
