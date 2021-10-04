class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() # nums 정렬
         
        for i in range(len(nums)-2): # num안 요소를 마지막에서 3번째까지 for문 반복
            # 2개 더할 왼쪽과 오른쪽 설정
            right = len(nums)-1
            left = i+1
            
            if i>0 and nums[i] == nums[i-1]: # 현재 인덱스에서의 num값이 이전 인덱스에서의 값과 같으면 다음 for문 진행
                continue
            
            # 왼쪽 인덱스가 오른쪽보다 작을 동안 while문 반복
            while left < right:
                sum = nums[left]+nums[right]+nums[i] # 합 구하기
                
                # 합의 결과에 따라 왼쪽이나 오른쪽 인덱스값 갱신
                if sum > 0: right-=1
                elif sum < 0: left+=1
                else:
                    ans.append([nums[i], nums[left], nums[right]]) # 합이 0일 경우 결과에 추가
                    
                    while left < right and nums[right] == nums[right-1]:# 오른쪽에서 나오는 중복 제거
                        right-=1
                    while left < right and nums[left] == nums[left+1]:# 왼쪽에서 나오는 중복 제거
                        left+=1
                    
                    left+=1
                    right-=1
                    
        return ans
