class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N = len(nums)

        # 앞서 있었던 3Sum 문제를 활용
        def threeSum(first, sub_target):
            sub_answer = set()
            for i in range(first+1, N-2):
                # 좌우 포인터를 유지하면서
                # 현재 3Sum이 원하는 값보다 작을 경우 왼쪽 포인터를 오른쪽으로 옮기고
                # 클 경우 오른쪽 포인터를 왼쪽으로 옮긴다
                left = i + 1
                right = N - 1
                while left < right:
                    sub_sum = nums[i] + nums[left] + nums[right]
                    if sub_sum == sub_target:
                        answer.add((nums[first], nums[i], nums[left], nums[right]))
                        left += 1
                    elif sub_sum < sub_target:
                        left += 1
                    else:
                        right -= 1
            
            return sub_answer
        
        answer = set()
        # 첫번째를 0번째부터 N-4번째까지 순회하며
        # target과 뺀 값을 3Sum으로 하는 경우의 수를 찾음
        for first in range(N-3):
            answer.union(threeSum(first, target-nums[first]))
        
        return [list(x) for x in answer]
