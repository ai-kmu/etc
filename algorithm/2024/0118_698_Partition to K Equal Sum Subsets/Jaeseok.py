# 정렬 후 이분탐색으로 풀려 했으나 이분 탐색으로는 각 subset의 최적의 해를 찾을 수 없음
# 가장 작은 수들 몇 개의 조합과 가장 큰 수 의 조합으로도 subset의 goal을 구성할 수 있기 때문

from bisect import bisect_left, bisect_right

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if k == 1:
            return True

        nums.sort()
        goal = sum(nums) // k
        print(goal)
        subsets = defaultdict()
        
        for i in range(k):
            subsets[i] = 0
            while subsets[i] != goal:
                if not nums:
                    break
                idx = max(0, bisect_right(nums, (goal - subsets[i])) - 1)
                print(nums, subsets[i], idx)
                # if idx >= len(nums):
                #     idx = -1
                subsets[i] += nums[idx]
                del nums[idx]
                    
        for k, v in subsets.items():
            if v != goal:
                return False
        return True
            

# 문제풀이는 backtracking으로 해야 함
# 정답 보고 주석 달았습니다 -> 리뷰 x
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, total = len(nums), sum(nums)

        # k개의 같은 sum을 가진 subset을 만들 수 있어야 함
        # 즉, 이게 불가능하면 무조건 False
        if total % k:
            return False
        
        # k개의 같은 sum = 평균
        target = total // k
        nums.sort(reverse=True)

        # visited : 방문 확인
        visited = [False] * n
        
        # DFS + backtracking
        def dfs(idx, cur_val, cur_subset):

            # k개만큼의 subset을 다 만들었으면 True 반환    
            if cur_subset == k:
                return True
            
            # 현재 subset에서 target만큼 수를 채워넣었으면 다음 subset으로 넘어감
            if cur_val == target:
                return dfs(0, 0, cur_subset + 1)
            '''
            현재 index에서 n까지 순회
            1. idx보다 이전의 nums[idx]는 다른 dfs에서 이미 순회했으므로 제외
            2. 이미 방문한 곳은 제외
            3. 현재 인덱스에서 더한 숫자가 target보다 큰 경우는 제외
            '''
            for i in range(idx, n):
                if visited[i] or (cur_val + nums[i] > target):
                    continue
                
                visited[i] = True
                if dfs(i + 1, cur_val + nums[i], cur_subset):
                    return True
                visited[i] = False
                
                # 현재 subset을 벗어나지 못하면 cur_val은 0인 상태로 남으므로 False
                if cur_val == 0:
                    return False

        return dfs(0, 0, 0)
