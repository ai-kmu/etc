class Solution:
    def getSkyline(self, bdgs: List[List[int]]) -> List[List[int]]:
        # 높이 변화를 만들어주는 리스트
        change = []
        for s, e, h in bdgs:
            change.append([s, 1, h])
            change.append([e, -1, h])
        # print(change)
        # [[2, 1, 10], [9, -1, 10], [3, 1, 15], [7, -1, 15], [5, 1, 12], [12, -1, 12], [15, 1, 10], [20, -1, 10], [19, 1, 8], [24, -1, 8]]
        change.sort(key=lambda x:[x[0], -x[1], -x[2]])

        answer = []
        heap = []
        resid = []
        for i, (p, f, h) in enumerate(change):
            # f(flag)에 따라 건물 높이 추가
            if f == 1:
                heapq.heappush(heap, -h)
            else:
                heapq.heappush(resid, -h)
            
            # resid는 버릴 건데, 높이가 같은 게 남아 있으면 같이 제거
            while len(resid) > 0 and heap[0] == resid[0]:
                heapq.heappop(heap)
                heapq.heappop(resid)

            # 다 지워졌으면 현재 위치는 건물 없음
            if len(heap) == 0:
                answer.append([p, 0])
            # 남아있다면
            else:
                # 조건
                if (i == 0  # 맨 처음이거나
                    or i == len(change) - 1  # 맨 마지막이거나
                    # 이미 있는 높이가 아닐 때만 높이 지정
                    or (-heap[0] != answer[-1][-1] and p != change[i+1][0])):
                   answer.append([p, -heap[0]])
        
        return answer

