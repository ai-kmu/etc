#문제 설명 :  각 인덱스마다 가능한 최대 점프 수가 적혀있는 리스트가 주어졌을 때, 마지막 인덱스까지 도착하기 위한 최소한의 점프 수를 구하는 문제

#해결 방법 : 점프 가능한 범위안의 인덱스 중에서 Greedy하게 또 다시 가장 점프를 많이 할 수 있는 인덱스에 도착해 점프하는 방법
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        answer=0 # 최소한의 점프 수
        max_jump=0 # 최대 점프 수 
        targetIdx=0 # 타겟 인덱스 
        nums_len=len(nums) #리스트 길이
        
        for i in range(nums_len-1): 
            max_jump= max(max_jump, i+nums[i]) # 점프를 해서 가장 멀리 도착할 수 있는 타겟 인덱스 구하기
            
            if i == targetIdx: #  점프를 해서 가장 멀리 도착할 수 있는 타겟 인덱스에 도착했다면
                answer += 1 # 점프 수 카운트 
                targetIdx=max_jump # 현재까지 지나온 것 중 가장 멀리 도착할 수 있는 인덱스로 타겟 인덱스 갱신
                
        return answer
            
            
        
