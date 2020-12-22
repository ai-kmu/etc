class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_list = [int(i) for i in nums]
        sorted_list.sort()
        s = 0
        e = len(list) - 1

        if nums == sorted_list:
            return 0

        while sorted_list[s] == nums[s]:
            s+=1

        while sorted_list[e] == nums[e]:
            e-=1

        return e-s+1

