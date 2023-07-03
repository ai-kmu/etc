class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        result = 0
        left = 0
        window_dic = {}  # sliding window 방식 사용.
        for right in range(len(nums)):  # 최대 right값=len(nums)-1
            try:
                window_dic[nums[right]]  # sliding window에서 오른쪽 부분의 수
            except:
                window_dic[nums[right]] = 0
            window_dic[nums[right]] += 1  # 슬라이딩윈도우 내부 포함된 숫자 빈도 증가
            while (
                max(window_dic.keys()) - min(window_dic.keys()) > 2
            ):  # subarray 조건 불충족시
                window_dic[nums[left]] -= 1  # 윈도우 내 숫자 빈도 감소

                if window_dic[nums[left]] == 0:  # 윈도우 내 해당 수가 등장하지 않으면
                    del window_dic[nums[left]]  # 슬라이딩윈도우에서 삭제

                left += 1  # 범위 줄여나감

            result += right - left + 1  # 가능한 subarray 수 추가

        return result
