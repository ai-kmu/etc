from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        candidates = {0: 1}
        
        for nums in [nums1, nums2, nums3, nums4]:
            new_candidates = defaultdict(int)
            # 모든 nums의 n에 대해
            for n in nums:
                # 기존 sum과 n을 더해 count만큼 경우의수를 추가
                for prev, count in candidates.items():
                    new_candidates[prev+n] += count
            candidates = new_candidates
        
        return candidates[0]
