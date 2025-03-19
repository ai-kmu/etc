# 솔류션 참고해서 풀이 안 해주셔도 괜찮습니다.
from math import floor
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        arr = list((*nums1, *nums2)) 
        arr.sort()
        idx = len(arr)
        
        if idx%2 == 0: 
            return (arr[int(idx/2-0.5)] + arr[int(idx/2+0.5)])/2

        return arr[int(floor(idx/2))]
