class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [(i, nums[i]) for i in range(len(nums))]
        print(new_nums)
        new_nums.sort(key=lambda x:x[1])
        print(new_nums)
        s = 0
        e = len(nums) - 1

        while s <= e:
            if new_nums[s][1] + new_nums[e][1] > target:
                e -= 1

            elif new_nums[s][1] + new_nums[e][1] < target:
                s += 1

            else:
                break

        return [new_nums[s][0], new_nums[e][0]]
        
