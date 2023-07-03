class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        @cache # 캐싱을 적용하여 실행속도 높이기 위해서
        def dfs(idx, x, y):
            if idx >= n: # idx가 list size이상이면 배열 범위를 넘어가는 것이므로 return 0
                return 0
            minx = min(x, nums[idx])
            maxy = max(y, nums[idx])
            if abs(minx - maxy) <= 2: # 최솟값과 최댓값을 찾아서 비교, why? -> Continuous Subarrays 조건에서 i <= i1, i2 <= j와 절댓값을 포함하기 때문
                return 1 + dfs(idx + 1, minx, maxy)  # idx의 다음 idx원소를 포함한 경우를 고려
            return 0
        sum = 0
        for i in range(n):
            sum += dfs(i, nums[i], nums[i]) # nums[i]가 포함 된 Continuous Subarrays 개수를 ans에 더함
                                            # 예를 들어, i가 0이라면 nums[0] == 5 이므로
                                            # [5], [5,4], [5,4,2], [5,4,2,4] 중 Continuous Subarrays 조건을 만족하는 배열의 갯수를 return 
        return sum
