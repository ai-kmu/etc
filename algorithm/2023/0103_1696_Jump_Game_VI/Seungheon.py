from collections import defaultdict

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        # dp이용

        # tmp_max의 개수를 세기 
        # num_dict의 value의 합은 k
        num_dict = defaultdict(int)

        # max값 과 num_dict 초기화
        tmp_max = nums[0]
        num_dict[nums[0]] += 1

        # 현재위치에 올 수 있는 가장 큰 값 찾기
        for i in range(1, len(nums)):

            # dictionarry 에서 범위 밖의 값 빼기
            if i > k:
                num_dict[nums[i-k-1]] -= 1
                if num_dict[nums[i-k-1]] == 0:
                    
                    # max값이 없어진다면 max값 update
                    del num_dict[nums[i-k-1]]
                    if nums[i-k-1] == tmp_max:
                        tmp_max = max(num_dict.keys())

            nums[i] += tmp_max
            tmp_max = max(nums[i], tmp_max)  
            num_dict[nums[i]] += 1

        return nums[-1]
