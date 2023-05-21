class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # sliding window 방식 사용
        start = 0
        
        answer = 0
        # num_zero: start와 end 사이의 zero의 개수
        num_zero = 0
        for end, n in enumerate(nums):
            if not n:
                # 이미 zero를 k개 만큼 썼을 경우
                # 제일 처음 zero를 제거하기 위해 start를 떙긴다
                if num_zero == k:
                    while nums[start]:
                        start += 1
                    start += 1
                else:
                    num_zero += 1
            answer = max(answer, end - start + 1)
                    
        return answer
