# 우선 그래프로 이해 할 것
# 여기서 해당 문제는 조금 특수한 그래프, 모든 노드가 한번의 input edge와 output edge만을 가짐

# 따라서 해당 문제는 가장 큰 Cycle을 찾으면 됨
# 단 이 때 같은 cycle에 있는 노드들은 어디에서 시작하든 같은 값을 가짐, 즉 한 cycle에서는 한번만 검사하면 됨
# 따라서 한 cycle을 돌 때 방문한 노드들을 모두 False로 바꾸어 그 노드들은 더이상 검사를 수행하지 않게 함



class Solution:
    def arrayNesting(self, nums):
        max_length = 0                  
        flag = [False] * len(nums)      #해당 노드를 체크했나 안했나 검사를 함

        for i in range(len(nums)):
            length = 0
            temp_location = nums[i]
            while(not flag[temp_location]): # 우선 temp_location으로부터 시작하는 cycle의 비용을 계산함
                flag[temp_location] = True  # 해당 cycle에 있는 node들은 모두 방문한것으로 표시, 즉 해당 cycle에 있는 node들로부터 시작하는 것은 더이상 계산하지 않겠다는 뜻
                temp_location = nums[temp_location]
                length+=1

            max_length = max(length, max_length)
        return max_length # 모든 cycle 중 최대 비용을 갖는 cycle을 return

