class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        # lru_cache 적용
        @lru_cache(None)
        def get_score_diff(left, right):
            # 숫자가 하나만 남은 경우
            if left == right:
                return nums[left]
            
            # 왼쪽을 고를 때와 오른쪽을 고를 때 중 최선 고르기
            pick_left = nums[left] - get_score_diff(left + 1, right)
            pick_right = nums[right] - get_score_diff(left, right - 1)
            
            return max(pick_left, pick_right)
        
        # 점수 차이가 0 이상이면 Player 1 승
        final_score = get_score_diff(0, n - 1) >= 0
        return final_score
