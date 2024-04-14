class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        # O(n^4) -> 당연히 시간초과
        # 두 수의 합을 0으로 만드는 경우로 간주하여 O(n^2)으로 해결

        result = 0
        nums_dict = defaultdict(int)

        # nums1과 nums2를 더한 값이 몇번 등장하였는지 기록
        for i in nums1:
            for j in nums2:
                nums_dict[i+j] += 1
                
        # 앞서 저장한 값의 반대인 경우 -> 0에 해당하므로 횟수 저장
        for i in nums3:
            for j in nums4:
                result += nums_dict[-(i+j)]
                
        return result
