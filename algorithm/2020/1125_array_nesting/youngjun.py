class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=0
        visited=[False]*len(nums) # 방문 했는지 체크
        
        length_list=[]
        
        for i in range(len(nums)):   
            length=0
            current_index=nums[i]
            while (not visited[current_index]): # 방문했으면 break
                visited[current_index]=True
                current_index=nums[current_index]
                length+=1
        
            length_list.append(length)
        answer=max(length_list) # 길이 중 제일 긴 것 계산 
        
        return answer