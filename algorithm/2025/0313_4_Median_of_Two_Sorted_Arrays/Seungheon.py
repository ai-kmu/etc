# failcode
# log(m+n)으로 해보려는데 실패함

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        # nums1의 중앙값을 구하고 nums2의 중앙값을 구하면, 그 사이에 전체 중앙값이 있다.

        # 중앙값 출력
        def median(nums, left, right):
            # 홀수
            if right-left % 2 == 0:
                return nums[(right + left) // 2]
            # 짝수
            else:
                return (nums[(right + left) // 2] + nums[(right + left) // 2 + 1]) / 2
        # 중앙값의 왼쪽 혹은 오른쪽 혹은 중앙값의 idx 출력
        def median_idx(nums, left, right, side==None):
            # 홀수
            if (right-left) % 2 == 0:
                return (right + left) // 2
            # 짝수
            else:
                if side == "left":
                    return (right + left) // 2)
                elif side == "right":
                    return (right + left) // 2 + 1
                else:
                    assert False
            
                
        nums1_left = 0
        nums2_left = 0
        nums1_right = len(nums1) - 1
        nums2_right = len(nums1) - 1
        while 1:
            # 중앙값과 idx 찾기
            nums1_median = median(nums1, nums1_left, nums1_right)
            nums2_median = median(nums2, nums2_left, nums2_right)
            # nums1의 중앙값과 nums2의 중앙값중 무엇이 더 큰지 확인

            if nums1_median > nums2_median: # nums1이 더크면 중앙값이 right
                # nums1_left = nums1_left
                nums2_left = median_idx(nums1, nums1_left, nums1_right, side="left")
                nums1_right = median_idx(nums2, nums2_left, nums2_right, side="right")
                # nums2_right = nums2_right
            elif nums1_median < nums2_median: # nums1이 더작으면
                nums1_left = median_idx(nums2, nums1_left, nums1_right, side="right")
                # nums2_left = nums2_left
                # nums1_right = nums1_right
                nums2_right = median_idx(nums2, nums2_left, nums2_right, side="left")     
            else: # nums1_median == nums2_median
                return nums1_median
            # 작은쪽은 중앙값으로 부터 오른쪽만 사용
            # 큰쪽은 중앙값으로부터 왼쪽만을 사용



