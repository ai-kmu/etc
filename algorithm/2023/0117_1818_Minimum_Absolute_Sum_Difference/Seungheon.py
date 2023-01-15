# fail code

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        sorted_num = sorted(list(set(nums1)))

        minimum = float('inf')
        
        # 가장 비슷한 값으로 대체하고 차이가 얼마나 줄어드는지 구함
        # 줄어드는 정도가 가장 큰 값을 찾아서 줄어든 차이만큼 sum에서 빼준다 
        
        max_difference = 0
        sum_difference = 0 
        idx = 0
        for i in range(len(nums1)):
            sum_difference += abs(nums1[i]-nums2[i])
            # sorted_num에서 j와 가장 비슷한 값 찾기
            # 비슷한 값중 원래값보다 작고 차이가 가장 많이나는것 찾기
            low = 0
            high = len(sorted_num) - 1
            mid = 0
            while low < high:
                mid = low + (high - low) // 2
                if sorted_num[mid] < nums2[i]:
                    low = mid + 1
                elif sorted_num[mid] > nums2[i]:
                    high = mid - 1
                else:
                    break    

            # nums1에서 j와 가장 비슷한 값을가진 idx : min_difference_idx
            min_difference_idx = mid
            for k in [mid-1, mid, mid+1]:
                if k < 0 or k > len(sorted_num)-1:
                    continue
                if abs(nums2[i]-sorted_num[k]) < abs(nums2[i]-sorted_num[min_difference_idx]):
                    min_difference_idx = k

            # 가장 비슷한 값으로 바꾸었을때 차이 구하기
            # 원래차이 - 바꾸었을 때 차이
            max_difference = max(max_difference, abs(nums2[i]-nums1[i]) - abs(nums2[i]-sorted_num[min_difference_idx])) 


        return (sum_difference - max_difference) % (10**9 + 7)
