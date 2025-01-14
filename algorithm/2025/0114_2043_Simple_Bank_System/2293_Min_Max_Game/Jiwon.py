class Solution:
    def minMaxGame(self, nums: List[int]) -> int:                
        num_list = nums
        while len(num_list) > 1:
            tmp = []
            for j in range(0, len(num_list) // 2):
                if j % 2 == 0:
                    tmp.append(min(num_list[2*j], num_list[2*j+1]))
                else:
                    tmp.append(max(num_list[2*j], num_list[2*j+1]))
            num_list = tmp
        return num_list[0]
