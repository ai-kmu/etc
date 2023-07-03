class Solution(object):
  
    def continuousSubarrays(self, nums):

        total=0
        # l에 슬라이싱해서 모든 경우의 수 넣어줌
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)-i):
                l.append(nums[i:len(nums)-j])
              
        # 만든 경우의 수를 for문으로 돌리며 하나씩 확인하면서,
        for i in range(len(l)):
            minx=min(l[i]) #그 안의 최소값과
            maxx=max(l[i]) # 최대값 구해서
            if abs(minx-maxx)<=2: # 차이가 2보다 작으면
                total+=1 # total에 1누적

        return total
