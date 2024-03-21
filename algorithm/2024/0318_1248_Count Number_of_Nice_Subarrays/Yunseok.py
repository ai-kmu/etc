class Solution:
    def is_odd(self, val):
        return val & 1

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odd_idx_list = [-1]  
        num_of_sub_arrays = 0           
        
        # 홀수 인덱스 저장
        for i in range(len(nums)):
            if self.is_odd(nums[i]):
                odd_idx_list.append(i)

        # 마지막 서브어레이 계산을 위해 
        odd_idx_list.append(len(nums))

        result = 0          
        
        if len(odd_idx_list) < k:
            return 0

        # 연속된 k개의 홀수를 가진 서브어레이 갯수 세기
        for i in range(1, len(odd_idx_list) - k):
            num_of_left = odd_idx_list[i] - odd_idx_list[i - 1]
            num_of_right = odd_idx_list[i + k] - odd_idx_list[i + k - 1]
            num_of_sub_arrays += num_of_left * num_of_right

        return num_of_sub_arrays
