class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):                          # 모든 값 비교
            for j in range(1,len(nums)):
                for k in range(2,len(nums)):
                    if i==j or j==k or i==k:                # 같은 index 생략
                        continue
                    now = nums[i]+nums[j]+nums[k]
                    if abs(now-target)<abs(answer-target):  # 현재값과 지금까지 최소값 비교  
                        answer = now
                    if answer==target:                      # target과 값이 같다면 종료
                        return answer
        return answer
