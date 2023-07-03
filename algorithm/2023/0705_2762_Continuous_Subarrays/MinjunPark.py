from collections import deque

class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            s, e = i, i # s == subarray의 시작, e == subarray의 끝
            minNum, maxNum = nums[s], nums[s] # initialize

            while e < len(nums): 
                if nums[e] > maxNum: # max값 갱신
                    maxNum = nums[e]
                
                if nums[e] < minNum:# min값 갱신
                    minNum = nums[e]
            
                if maxNum - minNum <= 2: # 조건에 부합하면 ans += 1
                    ans += 1
                else: # 부합하지 않으면 i+1번쨰 원소를 시작으로하는 subarray를 계산
                    break

                e += 1
                
        return ans
