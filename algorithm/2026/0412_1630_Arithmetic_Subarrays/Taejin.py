class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ret = []
        
        def is_arithmetic(arr):
            if len(arr) < 3:
                return True

            else:
                for i in range(1, len(arr) - 1):
                    if arr[i] - arr[i - 1] != arr[i + 1] - arr[i]:
                        return False

            return True

        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            ret.append(is_arithmetic(temp))

        return ret
