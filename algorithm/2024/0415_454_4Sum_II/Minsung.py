class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        '''
        1. nums1~4 4개의 list를 두 개씩 나누어 각각에 대하여 가능한 합 저장 -> sum1, sum2
        2. sum1을 기준으로 문제 조건에 부합하는 value가 sum2에 몇개 있는지 binary search
        '''
        sum1 = list()
        sum2 = list()

        for n1 in nums1:
            for n2 in nums2:
                sum1.append(n1+n2)  # nums1, nums2의 모든 합 저장
        for n3 in nums3:
            for n4 in nums4:
                sum2.append(n3+n4)  # nums1, nums2의 모든 합 저장

        sum2.sort()  # binary search를 위해 정렬 

        ans = 0        
        
        for value in sum1:
            target = 0 - value  # sum2에서 찾아야 하는 값 
            
            left = 0
            right = len(sum2) - 1
            
            while left <= right:  # 중복될 수 있는 target 위치 중, 가장 왼쪽에 있는 index 찾기 
                mid = (left+right) // 2
                if sum2[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            target_start = left  

            left = 0
            right = len(sum2) - 1
            while left <= right:  # 중복될 수 있는 target 위치 중, 가장 오른쪽에 있는 index 찾기 
                mid = (left+right) // 2
                if sum2[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            target_end = right
            
            ans += target_end - target_start + 1  # target 값을 만족하는 갯수
            
        return ans
