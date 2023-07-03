# 기본적으로 left는 0, right는 1부터 시작한 상태에서 right를 1씩 증가시킴
# for문 마지막에 ans는 right가 추가됨에 따라 늘어나는 가짓수를 더해줌

# 숫자 하나가 추가되었을 때 가짓수가 증가하는 범위는 최소 1에서 최대 n임
# 1인 경우는 이전 window 모두가 현재 숫자와 3이상 차이가 나는 경우
# 2인 경우는 바로 이전 숫자를 제외하고는 이전 window 모두가 현재 숫자와 3이상 차이가 나는 경우
# ...
# 2인 경우는 바로 이전 숫자를 제외하고는 이전 window 모두가 현재 숫자와 2이하로 차이가 나는 경우


class Solution:
    def continuousSubarrays(self, nums):
        left = 0
        ans = 0
        new_window = lambda num: [num - 2, num + 2] # window를 다시 만듦
        renew_window = lambda window, num: [max(window[0], num - 2), min(window[1], num + 2)]  # p_range에 num을 포함하여 재조정

        p_range = new_window(nums[0]) # possible range

        for right in range(1, len(nums)):
            if p_range[0] <= nums[right] <= p_range[1]:
                p_range = renew_window(p_range, nums[right]) # 새로 추가된 숫자를 포함하여 window를 재조정
            else:
                p_range = new_window(nums[right])
                left = right
                while p_range[0] <= nums[left-1] <= p_range[1]:
                    left -= 1

                p_range = renew_window(p_range, nums[left])
            
            ans += right - left + 1

        return ans + 1
