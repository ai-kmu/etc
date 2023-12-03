# 오랜만에 DP 풀려니까 안풀리네요 답봤습니다. 리뷰 안해주셔도 돼요
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 각각의 홀수 번째와 짝수 번째 원소들의 누적 합 계산
        odd_sum, even_sum = [0] * (n + 1), [0] * (n + 1)
        for i in range(n):
            odd_sum[i + 1] = odd_sum[i] + (nums[i] if i % 2 == 1 else 0)
            even_sum[i + 1] = even_sum[i] + (nums[i] if i % 2 == 0 else 0)
        
        count = 0  
        
        # 각 원소를 제거했을 때 배열이 공평한 배열이 되는지 확인
        for i in range(n):
            odd_left = odd_sum[i]  
            odd_right = odd_sum[-1] - odd_sum[i + 1]  
            even_left = even_sum[i]  
            even_right = even_sum[-1] - even_sum[i + 1]  
            
            # 현재 원소를 제거하고 공평한 배열이 되는 경우의 수를 센다.
            if odd_left + even_right == even_left + odd_right:
                count += 1
        
        return count
