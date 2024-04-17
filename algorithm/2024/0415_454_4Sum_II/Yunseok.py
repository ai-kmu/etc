class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum_dict = {}
        # 파트 1: nums1과 nums2로 가능한 모든 합의 조합을 사전에 저장
        for num1 in nums1:
            for num2 in nums2:
                sum_result = sum_dict.get(num1 + num2, 0)
                sum_dict[num1 + num2] = sum_result + 1

        # 파트 2: nums3과 nums4로 만든 합으로 nums1, nums2 합의 음수값을 찾아 카운트
        for num3 in nums3:
            for num4 in nums4:
                target_result = sum_dict.get(-(num3 + num4))
                if target_result is not None:
                    count += target_result

        return count
