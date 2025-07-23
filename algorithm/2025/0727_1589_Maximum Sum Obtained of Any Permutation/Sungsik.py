from collections import deque
import heapq

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # frequency가 가장 많은 index에 가장 큰 num을 배치하면 됨
        n = len(nums)
        frequency = [0] * n
        requests.sort()
        requests = deque(requests)
        tmp_requests = []

        # 아래와 같이 O(n^2)으로 짜니까 time error 남
        # for i, j in requests:
        #     for k in range(i, j+1):
        #         frequency[k] += 1

        # index를 순회하면서 현재 index에 request가 몇개 포함되는지로 구현
        # request를 sort하고 가장 왼쪽꺼의 시작이 현재 index보다 작거나 같으면 포함시킴
        # tmp_requests에서 가장 작은 end값이 현재 index보다 작으면 제외시킴
        for i in range(n):
            while requests and requests[0][0] <= i:
                heapq.heappush(tmp_requests, requests.popleft()[1])
            while tmp_requests and tmp_requests[0] < i:
                heapq.heappop(tmp_requests)
            
            frequency[i] = len(tmp_requests)

        nums.sort()
        frequency.sort()
        return sum([x * y for x, y in zip(nums, frequency)]) % (10**9 + 7)   
