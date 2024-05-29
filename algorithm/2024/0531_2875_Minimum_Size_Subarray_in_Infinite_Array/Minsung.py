class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        ans1 = 0  
        if sum(nums) < target:
            ans1 += target // sum(nums) * len(nums)  # target이 현재 nums의 합보다 크다면 down-scaling 진행
            target = target  % sum(nums)  # down-scaling 과정에서 사용한 개수는 정답에 포함되어야 함

            if target == 0:  # 이후에 아무 값도 더해주지 않아도 된다면 그대로 retrun
                return ans1

        nums.extend(nums)  
        cul_nums = [0]  # 누적합 저장
        for i in nums:
            cul_nums.append(cul_nums[-1] + i)
        
        ans2 = int(1e6)  # 누적합 중에서 target을 만족하는 최소 길이 저장, 문제조건 상에서 가능한 최대값으로 초기화
        for i, cur in enumerate(cul_nums):  
            left = i + 1
            right = len(cul_nums) - 1
            while(left <= right):  # 현재 index 기준으로 target을 만족하는 index 찾기 (이진탐색)
                mid = (left + right) // 2
                if cul_nums[mid] - cur == target:
                    ans2 = min(ans2, mid-i)
                    break
                elif cul_nums[mid] - cur > target:
                    right = mid - 1
                else:
                    left = mid + 1
        
        if ans2 == int(1e6):  # target을 만족하는 sub-array를 구할 수 없다면 -1 return
            return -1
        return ans1 + ans2  # target을 만족하는 sub-array를 구할 수 있다면 앞서 구한 ans1과 +
