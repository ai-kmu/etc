class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l = len(nums) # nums 길이 저장
        count = 0 # jump 횟수 저장할 변수
        farthest = 0 # 인덱스마다 최대로 갈 수 있는 step
        now = 0 # 현 위치 저장하기 위한 변수
        
        for i in range(l-1):
            farthest = max(farthest, i + nums[i]) # 모든 인덱스를 참조할 때 가장 멀리 갈 수 있는 인덱스 위치 갱신 후 저장
            if i == now: # 만약 현재 참조하는 인덱스가 현 위치 now랑 같은 경우
                count += 1 # 이 때 jump가 하나인 것이다.
                now = farthest # 현 위치 now를 갱신한 farthest로 변경
                
        return count; # 최소 jump수 출력
        
