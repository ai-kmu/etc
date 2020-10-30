# 이게 될 줄 몰랐어요...

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        first_num = True
        if len(nums) == 3:                                            # nums의 길이가 3인 경우, 3개의 합 반환
            return nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):                                  
            for j in range(i+1, len(nums)-1):
                if j == len(nums)-1:                                  # 두 번째 숫자가 nums의 마지막 숫자인 경우 다음으로 넘어감 
                    break
                for k in range(j+1, len(nums)):
                    if first_num:                                     # 처음 저장하는 경우 answer에 세 수의 합을 저장
                        answer = nums[i] + nums[j] + nums[k]
                        first_num = False
                    else:                                             # 처음 저장하는게 아닌 경우 
                        temp = nums[i] + nums[j] + nums[k]            # temp에 새 수의 합을 저장 
                        if abs(target - answer) > abs(target - temp): # 절대값을 이용하여 타겟과의 차이가 더 작은 수를 answer에 저장
                            answer = temp
                    if answer == target:                              # answer가 target과 같은 경우 answer 반환
                        return answer
        return answer
