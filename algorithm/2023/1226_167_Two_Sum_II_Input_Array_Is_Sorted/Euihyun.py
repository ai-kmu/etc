
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        num = len(numbers)
        start = 0
        end = num - 1
        
        # 이진탐색 mid를 두개 더한값으로 설정해서 풀이
        while start <= end:
            mid = numbers[start] + numbers[end]
            # 정답이면 그만
            if mid == target:
                return [start+1, end+1]
            # 작으면 키우고
            elif mid < target :
                start += 1
            # 크면 작게
            else:
                end -= 1
        
                    
        return []
        
        
