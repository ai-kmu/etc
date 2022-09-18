class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 맨 앞 값이 맨 마지막 값보다 작을 때는  rotation이 되지 않은 오름차순이기때문에 맨 앞값 return 
        if nums[0] < nums[-1]:
            return nums[0]
        else:
            low = 0
            high = len(nums)
            minimum = nums[0]
            while high - low > 2 :
                
                mid = (low + high) // 2
                # 중간값보다 최소값이 더 작다면 high 범위를 축소시켜주고 최소값 갱신
                if nums[mid] < minimum :
                    high = mid + 1
                    minimum = nums[mid]
                elif nums[mid] == minimum:
                    # 최소값과 중간값이 같은 값일 때 처리해주는 부분 구현 실패..
                # 중간값보다 최소값이 더 크다면 low 범위 변경
                else:
                    low = mid
                
            # 최소값은 low와 high 사이 nums에서 맨 뒷값이 됨 
            minimum = nums[low:high][-1]
            
                
        return minimum
