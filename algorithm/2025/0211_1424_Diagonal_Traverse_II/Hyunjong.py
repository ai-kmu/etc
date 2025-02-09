from collections import defaultdict
class Solution(object):
    def findDiagonalOrder(self, nums):
        map = defaultdict(list)
        
        # 대각선 요소 저장
        for row in range(len(nums)):
            for col in range(len(nums[row])):
                map[row + col].append(nums[row][col])
        
        aws = []
        for key in sorted(map.keys()):
            # 각 대각선은 역순으로 추가
            aws.extend(reversed(map[key]))
        return aws
