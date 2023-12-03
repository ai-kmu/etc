class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        odd_sum_right, even_sum_right = 0, 0
        odd_sum_left, even_sum_left = 0, 0
        prefix_sums = []
        result = 0
        
        # 배열의 뒤에서부터 시작하여 오른쪽 부분 배열의 합을 계산
        for i in range(len(nums)-1, -1, -1):
            prefix_sums.append([odd_sum_right, even_sum_right, odd_sum_left, even_sum_left])
            # 현재 인덱스가 홀수면 홀수 합에 더하고, 짝수면 짝수 합에 더함
            if i % 2:
                odd_sum_right += nums[i]
            else:
                even_sum_right += nums[i]
        
        # 배열을 뒤집어서 왼쪽 부분 배열의 합을 계산
        prefix_sums = prefix_sums[::-1]
        for i in range(len(nums)):
            prefix_sums[i][2], prefix_sums[i][3] = odd_sum_left, even_sum_left
            # 현재 인덱스가 홀수면 홀수 합에 더하고, 짝수면 짝수 합에 더함
            if i % 2:
                odd_sum_left += nums[i]
            else:
                even_sum_left += nums[i]
        
        # 각 인덱스에서 왼쪽 부분 배열과 오른쪽 부분 배열의 합이 동일한지 확인하면서 답을 계산
        for i in range(len(nums) - 1, -1, -1):
            if prefix_sums[i][2] + prefix_sums[i][1] == prefix_sums[i][3] + prefix_sums[i][0]:
                result += 1
                
        return result
