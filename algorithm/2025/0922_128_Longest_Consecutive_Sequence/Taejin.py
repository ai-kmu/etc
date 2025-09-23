from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 중복값은 제외해도 됨 -> set
        # 최대 연속 수열 길이 계산을 위해 정렬 -> new_nums
        # 두 연속 수열의 요소 차이는 항상 같음
        # 0부터 시작하는 연속 수열 - 중복 제거된 정렬된 nums 수열 계산 -> cnt_nums
        # cnt_nums 요소 갯수 카운트 값 = new_nums의 연속 부분 수열 길이들
        # cnt_nums의 요소 카운트 해서 가장 많은 요소 반환

        new_nums = sorted(list(set(nums)))
        cnt_nums = [i - new_nums[i] for i in range(len(new_nums))]
        cnt = Counter(cnt_nums)
        return max(cnt.values()) if cnt else 0
