class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums에서 증가하는 subsequence 찾기
        # 중간 요소 뛰어넘어도 됨.
        # O(n^2) 느림
        answers = [1 for _ in nums] # answers 초기화
        n = len(nums)
        
        for i in range(n):
            for j in range(i): # nums[:i]까지 탐색해서 확인
                if nums[j] < nums[i]: # 본인보다 작으면 업데이트
                    # 이전순서에서 구한 값과 현재의 업데이트 값을 비교하여 계산
                    answers[i] = max(answer[i], answers[j] + 1) 
        return max(answers)
        
