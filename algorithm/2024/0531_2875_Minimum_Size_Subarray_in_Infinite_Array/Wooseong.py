class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        '''
        target을 만들기 위한 리스트를
        infinite_nums에서 [nums의 뒷 부분] + N * [nums] + [nums의 앞 부분]과 같이 찢어서 생각하면 된다.

        ex)
        nums = [2,4,7,7,1,6,3]; target = 35이라 하자.
        total = 30이므로
        ans = 7; target = 5로 재설정된다.
        이 5를 [2,4,7,7,1,6,3,2,4,7,7,1,6,3]에서 적절히 찾으면 된다.
                           ___ 여기를 택하면 된다.
        즉, 우리가 취한 infinite_nums는 [3] + [2,4,7,7,1,6,3] + [2] 인 거고,
        답은 7 + 2이다.

        만약 target이 41이라면
        11을 [2,4,7,7,1,6,3,2,4,7,7,1,6,3]에서 적절히 찾으면 된다.
               ___(정답) _____(오답)
        따라서 그냥 찾는 게 아니라, 어디가 shortest인지도 확인해야됨
        '''

        # 특수 케이스
        # 1. 숫자 하나로 처리되는 경우
        if target in nums:
            return 1
        # 2. N바퀴로 처리되는 경우
        total = sum(nums)
        count = len(nums)
        N, mod = divmod(target, total)
        if mod == 0:
            return N * count

        # ans, target 재설정 및 리스트 두 개 붙이기
        ans = N * count
        target -= total * N
        bi_nums = nums + nums
        
        # while을 위한 설정
        n = 2 * count
        i = j = sum_ = 0
        rem = float('inf')
        
        # 이건 결국 가능한 모든 경우를 다 찾고, 그 중 짧은 걸 갖고 오는 거임
        while j < n:
            # nums의 처음부터 끝까지 다 더하고, 다시 처음부터 더함
            # 그러면 결국 뒷부분 + 앞부분 꼴로 남게 됨
            sum_ += bi_nums[j]
            while sum_ > target:
                sum_ -= bi_nums[i]  # 넘치면 앞 부분을 제거 함
                i += 1
            
            # 이전에 찾은 답과 현재 길이 (j - 1 + 1)를 비교
            if sum_ == target:
                rem = min(rem, j - i + 1)
            j += 1

        # rem이 갱신 안 돼서 inf 그대로면 -1 반환
        # 갱신 됐으면 아까 구해둔 ans에 더해서 반환
        return -1 if rem == float('inf') else ans + rem
