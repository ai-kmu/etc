class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 정렬하고 순차적으로 비교함
        # 중복방지 정답을 위해 set 생성
        nums.sort()
        ans = set()

        # 전체를 돌면서 포인터를 움직임
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = i + 1
                l = j - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]

                    # 타겟이랑 같으면 ans 에 추가해주고 포인터 이동
                    if sum == target:
                        ans.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    # 타겟보다 작으면 k를 키워줌
                    elif sum < target:
                        k += 1
                    # 타겟보다 크면 l을 줄여줌
                    elif sum > target:
                        l -= 1
                    
        return ans
