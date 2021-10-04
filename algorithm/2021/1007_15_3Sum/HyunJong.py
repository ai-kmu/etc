class Solution(object):
    def threeSum(self, nums):
        nums.sort() ##순서 정리
        result = set() ## 같은 배치 다른 요소 제거용
        check = {} ## 2번째 포인터 이전 발생값 제거용
        for i in range(len(nums)):
            check[nums[i]] = i ## nums 원소에 중복없이 순서 부여
        for i in range(len(nums)): ## 포인터 1
            if i != 0 and nums[i] == nums[i-1]: ## 0 이 아닌데 이전 값과 동일하면 패스(중복 패스)
                continue
            twoSum = -nums[i] ##첫번째 값
            for j in range(i+1, len(nums)): ##포인터 2
                target = twoSum - nums[j] ## 두번째 값 설정
                if target in check and check[target] > j: ## 첫번째 두번째 더한 음수 값이 check에 있으면 성공
                    result.add((-twoSum, nums[j], target)) ## 정답에 추가
        return result
