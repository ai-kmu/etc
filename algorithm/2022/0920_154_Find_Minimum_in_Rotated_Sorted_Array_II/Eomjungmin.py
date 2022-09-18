class Solution:
    def findMin(self, nums: List[int]) -> int:
        ind = self.find_index(nums)
        if ind==-1 or ind==len(nums)-1:
            return nums[0]
        else:
            return nums[ind+1]
        
    # 이진 탐색을 이용하여 nums의 인덱스 탐색
    def find_index(self,nums):
        l = 0
        r = len(nums)-1
        while l<r:
            m = l+(r-l)//2 # 중간 인덱스
            
            # nums[m]이 nums[m+1]보다 크다는 것은 중간에서 오른쪽 부분이 다시 오른차순이므로 m+1부분이 최소값
            if m < r and nums[m] > nums[m+1]:
                return m
            
            # nums[m]이 nums[m-1]보다 작다는 것은 중간에서 왼쪽 부분이 내림차순이므로 m부분이 최소값
            if m > l and nums[m] < nums[m-1]:
                return m-1
            
            # m,r,l 인덱스에서 nums 값이 모두 같은경우 오름차순, 내림차순을 판단할 수가 없으므로 
            # 탐색하는 범위를 줄여야 함
            if nums[m] == nums[l] and nums[m] == nums[r]:
                if nums[r] < nums[r-1]:
                    return r-1
                else:
                    r = r-1
                    
                if nums[l] > nums[l+1]:
                    return l
                else:
                    l = l+1
            
            # (왼쪽 부분이 오름차순 or l과 m에서의 nums값이 같음) and (m에서 nums값이 r에서 보다 큰 경우)
            # 중간에서 오른쪽 부분만 보면 되므로 왼쪽 부분 l을 변경
            elif nums[l] < nums[m] or nums[l] == nums[m] and nums[r] < nums[m]:
                l = m+1
            
            # 나머지의 경우 오른쪽 r부분을 변경
            else:
                r = m-1
        return -1
        
