import heapq

# binary search를 쓰면 복잡도를 더 개선할 수 있을 것으로 보임
# 현재 O(log (m+n)) 조건을 만족하지는 못함
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_list = nums1
        total_list.extend(nums2)
        heapq.heapify(total_list)
        
        num_of_list = len(total_list)
        range_val = num_of_list // 2 + 1
        if num_of_list % 2 == 0:
            sum_val = 0
            for idx in range(range_val):
                elem = heapq.heappop(total_list)
                if idx >= range_val - 2:
                    sum_val += elem
            return sum_val / 2.0
        else:
            for idx in range(range_val):
                elem = heapq.heappop(total_list)
                if idx == range_val - 1:
                    return float(elem)


        return 0
