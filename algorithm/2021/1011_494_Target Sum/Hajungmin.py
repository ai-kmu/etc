class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 재귀함수에서 중복 연산을 하지 않을 수 있도록 도와주는 데코레이터 함수
        # 이게 없으면 time limit에러가 남
        @cache
        # index와 현재까지 합을 이용하여 재귀 함수를 구현
        def find_target(i, curr):
            # 만약 현재 index가 nums의 길이와 같고 현재까지 합이 target과 같다면 1을 반환
            if i == len(nums) and curr == target:
                return 1
            
            # 만약 현재 index는 nums의 길이와 같지만 합은 같지 않을 경우 0을 반환
            elif i == len(nums):
                return 0
            
            else:
                # count를 0으로 두고 target sum을 만족하는 식의 개수를 셈
                count = 0
                # 현재 index값과 현재까지의 합에 다음 index의 값을 더할 경우를 재귀함수로 구현
                count += find_target(i + 1, curr + nums[i])
                # 현재 index값과 현재까지의 합에 다음 index의 값을 뺄 경우를 재귀함수로 구현
                count += find_target(i + 1, curr - nums[i])
            # 총 count를 반환
            return count
        
        # 처음 위치인 (0, 0)에서 시작
        return find_target(0, 0)
