class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # merged_arr = list(sorted(nums1 + nums2))
        # total_len = len(nums1) + len(nums2)
        # mid = (total_len - 1) / 2

        # if mid % 1:
        #     return sum(merged_arr[int(mid): int(mid + 1) + 1]) / 2

        # return merged_arr[int(mid)]


        def get_median(arr1, arr2, k):
            idx1, idx2 = 0, 0  # 두 배열의 현재 탐색 위치
            
            while True:
                # arr1이 끝난 경우, arr2에서 k번째 원소 반환
                if idx1 == len(arr1):
                    return arr2[idx2 + k - 1]
                # arr2가 끝난 경우, arr1에서 k번째 원소 반환
                if idx2 == len(arr2):
                    return arr1[idx1 + k - 1]
                # k가 1이면, 두 배열의 첫 번째 원소 중 작은 값을 반환
                if k == 1:
                    return min(arr1[idx1], arr2[idx2])

                # k // 2 번째 원소를 각각 확인
                new_idx1 = min(idx1 + k // 2, len(arr1)) - 1
                new_idx2 = min(idx2 + k // 2, len(arr2)) - 1
                pivot1, pivot2 = arr1[new_idx1], arr2[new_idx2]

                # pivot1이 pivot2보다 작다면, arr1의 해당 부분을 버림
                if pivot1 <= pivot2:
                    k -= (new_idx1 - idx1 + 1)
                    idx1 = new_idx1 + 1
                else:  # pivot2가 pivot1보다 작다면, arr2의 해당 부분을 버림
                    k -= (new_idx2 - idx2 + 1)
                    idx2 = new_idx2 + 1

        total_len = len(nums1) + len(nums2)

        if total_len % 2 == 1:  # 원소 개수가 홀수
            return float(get_median(nums1, nums2, total_len // 2 + 1))
        else:  # 원소 개수가 짝수
            left_median = get_median(nums1, nums2, total_len // 2)
            right_median = get_median(nums1, nums2, total_len // 2 + 1)
            return (left_median + right_median) / 2
