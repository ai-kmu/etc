class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 홀수의 index를 구해놓음
        odds = [i for i, num in enumerate(nums) if num % 2] + [len(nums)]
        
        answer = 0
        left = -1
        
        for i, odd in enumerate(odds[:-k]):
            # 홀수를 k개 포함하는 array인 odds[i] ~ odds[i+k-1]를 포함하는 경우의 수를 구해서 answer에 더해줌
            answer += (odd - left) * (odds[i+k] - odds[i+k-1])
            left = odd
            
        return answer
