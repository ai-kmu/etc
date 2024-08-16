class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 정렬
        nums = sorted(nums)
        
        # 음수 몇 갠지 찾기
        for i, num in enumerate(nums):
            if num >= 0:
                num_negs = i
                break
        else:
            num_negs = len(nums)
        
        # 뒤집는 횟수가 음수 개수보다 작으면
        if k <= num_negs:
            # 앞에 거 (절댓값 큰 거) k개 뒤집기
            answer = sum(nums[k:]) - sum(nums[:k])
        # 더 많으면
        # 1. 음수 다 뒤집기
        # 2. 남은 건 2번 씩 해서 아무 것도 아닌 척하기
        # 3. 1개가 남으면 절댓값 제일 작은 거 뒤집고 끝내기
        else:
            # 음수 다 뒤집고 남은 횟수가 홀수인가? -> 절댓값 제일 작은 거 찾기
            if (k - num_negs) % 2:
                # 음수가 없을 경우 첫 번째 수가 절댓값 제일 작음
                if num_negs == 0:
                    min_abs = nums[0]
                # 음수만 있을 경우 마지막 수가 절댓값 제일 작음
                elif num_negs == len(nums):
                    min_abs = -nums[-1]
                # 음수가 있을 경우 마지막 음수와 첫 번째 양수 비교
                else:
                    min_abs = min(-nums[num_negs - 1], nums[num_negs])
                
                # 총합은 전체 절댓값 합에서 혼자 음수 된 애 두 번 빼기
                answer = sum(abs(num) for num in nums) - 2 * min_abs
            
            # 음수 다 뒤집고 남은 횟수가 짝수인가? -> 답은 절댓값 합
            else:
                answer = sum(abs(num) for num in nums)
        
        return answer
            
