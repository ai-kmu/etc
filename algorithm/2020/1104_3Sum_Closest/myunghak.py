class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = sum(nums[:3])

        for i in range(1, len(nums)):
            left,right = 0,len(nums)-1 # 정렬 후 왼쪽 오른쪽으로부터 한칸씩 줄임(target보다 작으면 왼쪽에서 target보다 크면 오른쪽에서)
            while(left !=i and right != i):
                Tans = nums[left] + nums[i] + nums[right]
                if abs(Tans - target) < abs(ans-target):
                    ans = Tans

                if target > Tans:
                    left +=1
                elif target < Tans:
                    right-=1
                elif target == Tans:
                    return target

        return ans
