class Solution:
    def jump(self, nums: List[int]) -> int:
        # answer을 초기화
        answer = [1000 for _ in range(len(nums))]
        answer[0] = 0 # 첫 index만 0
        for i in range(len(nums)):
            for j in range(i+1, i+nums[i]+1): # i에서 갈 수 있는 모든 index계산
                if j < len(nums): # 범위안에 있을 경우
                    answer[j] = min(answer[i]+1, answer[j]) # 현재 answer[j]보다 i번째에서 +1번 한게 더 작다면 그것을 선택
        
        return answer[-1] # 마지막에 도달했을 때의 최소 횟수 출력
        
