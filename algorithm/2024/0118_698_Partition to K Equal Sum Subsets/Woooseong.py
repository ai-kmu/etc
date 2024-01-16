class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 무조건 가능
        if k == 1:
            return True
        
        total = sum(nums)
        # 무조건 불가능
        if total % k:
            return False

        # 가능하려면 sum이 target인 리스트들로 쪼개야함
        target = total // k
        # 현재 시점 쪼개진 리스트들의 합
        sum_sub = [0] * k
        
        # 큰 수부터 사용: 원소가 하나짜리도 가능하기 때문
        nums.sort(reverse=True)
        
        # DFS를 이용한 Backtracking
        # 리스트들로 "쪼개는" 게 아니라
        # 각 원소들을 각각의 리스트에 "찔러넣어보는" 방식
        # i: 찔러 넣어질 원소
        # j: 찔려질 리스트
        def recursive(i):
            # 더 이상 찔러 넣을 원소가 없음
            if i == len(nums):
                return True
            
            # 리스트에 하나씩 찌르기
            for j in range(k):
                # 합이 넘어가면 미련 없이 다음으로
                if sum_sub[j] + nums[i] > target:
                    continue

                # 안 넘어가면
                else:
                    sum_sub[j] += nums[i]   # 찔러놓고
                    if recursive(i + 1):    # 다음 원소 찌르러 가기
                        return True         # 성공하면 끝
                    sum_sub[j] -= nums[i]   # 실패했으면 찔렀던 원소 회수
                    
                    # TLE 때문에 추가한 부분
                    # 회수 했더니 빈 리스트가 됐다
                    # -> 리스트에 처음으로 들어가는 거다
                    # -> 여기서 안 됐으면 다른 데서도 안 된다
                    # -> 애초에 글러 먹은 원소다 => break
                    if sum_sub[j] == 0:
                        return False

            return False  # True를 만나지 못했다는 것, False라는 것
        
        return recursive(0)
