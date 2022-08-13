class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
      
        # 기본적으로 가질 수 있는 subsequence 거리 1씩을 만들어 줌
        memo = [1] * len(nums)

        # memo 갱신은 index의 맨 마지막부터 처음으로 거꾸로 이루어짐
        for i in range(len(nums) - 1, -1, -1):
            # i보다 큰 인덱스부터 마지막까지 탐색하면서
            for j in range(i + 1, len(nums)):
                # 만약 nums의 i번째 요소가 탐색중인 j번째 요소보다 작다면
                # ex) 예를 들어 i = 5일 때, j는 6이거나 7일 수 있으며, 둘 다 nums의 i번째 요소가 탐색중인 j번째 요소보다 작다.
                if nums[i] < nums[j]:
                    # 앞에서 갱신시킨 subsequence의 거리를 비교하면서, max값을 구해준다.
                    memo[i] = max(memo[i], 1 + memo[j])
                else:
                    continue

        return max(memo)
