# 문제에서 시간복잡도 제한한 거 무시하고 풀라고 하길래 그냥 풀었어용......
# 이렇게 풀라고 낸 게 아닌 거 같긴한데... ^^

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        num_len = len(num)
        tmp = num_len//2
        if num_len % 2 == 1:
            return num[tmp]
        else:
            ans = num[tmp - 1] + num[tmp]
            return ans/2
