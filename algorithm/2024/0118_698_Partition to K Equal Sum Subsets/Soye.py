class Solution:
    # 주어진 배열(nums)을 k 개의 부분집합으로 나눌 수 있는지 확인하는 함수
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 기본적인 예외 처리: k가 1이면 언제나 True를 반환할 수 있음
        if k == 1:
            return True
        
        # 배열의 총 합과 길이 계산
        total = sum(nums)
        n = len(nums)
        
        # 총 합이 k로 나누어 떨어지지 않으면 불가능하므로 False 반환
        if total % k != 0:
            return False
        
        # 배열을 내림차순으로 정렬하여 큰 값부터 처리
        nums.sort(reverse=True)
        
        # 각 부분집합의 평균 값 계산
        average = total // k
        
        # 가장 큰 값이 평균보다 크면 불가능하므로 False 반환
        if nums[0] > average:
            return False
        
        # 방문 여부를 나타내는 리스트 초기화
        visited = [False] * n
        
        # 깊이 우선 탐색을 통해 부분집합을 구함
        def dfs(cur, begin, k):
            # k가 0이 되면 모든 부분집합이 구해졌으므로 True 반환
            if k == 0:
                return True
            # 현재 합이 평균을 초과하면 더 이상 진행할 필요가 없으므로 False 반환
            if cur > average:
                return False
            # 현재 합이 평균과 일치하면 다음 부분집합을 찾기 위해 재귀 호출
            elif cur == average:
                return dfs(0, 0, k - 1)
            # 배열을 탐색하며 가능한 부분집합을 찾음
            for i in range(begin, n):
                if not visited[i]:
                    # 현재 원소를 방문 표시하고 재귀 호출
                    visited[i] = True
                    if dfs(cur + nums[i], i + 1, k):
                        return True
                    # 재귀 호출이 실패한 경우 방문 표시를 취소
                    visited[i] = False
            # 모든 경우에 대해 부분집합을 찾지 못한 경우 False 반환
            return False
        
        # 초기 호출: 합 0, 시작 인덱스 0, 남은 부분집합의 수 k
        return dfs(0, 0, k)

        
