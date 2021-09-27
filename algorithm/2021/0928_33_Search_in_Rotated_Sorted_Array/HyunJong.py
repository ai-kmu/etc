#runtime over
class Solution(object):
    import bisect
    def search(self, nums, target):
        def argmin(a):
            return min(range(len(a)), key=lambda x: a[x])
        min_index=argmin(nums)
        before = nums[min_index:]
        after = nums[:min_index]
        flag = False
        if (before[-1]<target):
            target_nums = after
        elif (before[-1]>target):
            target_nums = before
            flag = True
        else:
            return target_nums
        pos = bisect.bisect_left(target_nums, target)
        if flag:
            result = len(after) + pos
        return result
