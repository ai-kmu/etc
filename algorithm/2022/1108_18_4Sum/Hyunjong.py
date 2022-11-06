class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # nums 정렬, 정렬해야 target과 비교하며 옮길 수 있다
        nums.sort()
        # 중복 답안 제거용
        res = set()
        # 첫 번째 숫자 선택
        for idx_1 in range(len(nums)):
            num_1 = nums[idx_1]
            
            # 두 번째 숫자 선택
            for idx_2 in range(idx_1 + 1, len(nums)):
                num_2 = nums[idx_2]
                # 세 번째, 네 번째 숫자 선택
                # 세 번째는 왼쪽에서 오른쪽으로, 네 번째는 반대로 동작 
                idx_3 = idx_2 + 1
                idx_4 = len(nums) -1

                # 서로 안 겹칠 때까지 반복
                while idx_3 < idx_4:
                    num_3 = nums[idx_3]
                    num_4 = nums[idx_4]
                    
                    # 정답 추출 조건
                    if num_1 + num_2 + num_3 + num_4 == target:
                        res.add((num_1, num_2, num_3, num_4))

                    # 숫자를 다 더한 값이 타겟보다 작으면 큰 숫자를 더해야 한다.
                    if num_1 + num_2 + num_3 + num_4 < target:
                        idx_3 += 1
                    # 숫자를 다 더한 값이 타겟보다 크면 더 작은 숫자를 더해야 한다.
                    else:
                        idx_4 -= 1
        return list(res)
                
