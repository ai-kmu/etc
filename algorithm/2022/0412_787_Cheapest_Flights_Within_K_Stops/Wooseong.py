from collections import defaultdict, deque

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        # graph로 변환: {parent:[child, price]}
        graph = defaultdict(list)
        for f, t, p in flights:
            graph[f].append((t, p))

        # node까지 가는 최소 cost list - 처음엔 inf로 초기화
        minCosts = [float('inf') for _ in range(n)]
        que = deque([(src, 0)])    # (to_node, price) - 현재 0번째 층

        # BFS
        stop = -1     # 0번째 층에서 시작해야 되니까 -1
        while que and stop < k :
            # 한 층 내려가기
            stop += 1
            
            # 같은 층에 있는 node의 개수
            howmany_level = len(que)
            for _ in range(howmany_level):
                # 하나 씩 뽑아서
                node, price = que.popleft()

                # 그 아래에 있는 (한 층 더 아래)
                for child, cost in graph[node]:
                    # 만약 그때까지의 costs보다 이 경로가 싸면
                    if price + cost < minCosts[child]:
                        minCosts[child] = price + cost    # update
                        que.append((child, price + cost)) # 걔네도 경로에 추가하기

        answer = minCosts[dst]
        return -1 if answer == float('inf') else answer

        '''질문
        마지막 두 줄을
        
        return -1 if minCosts[dst] == float('inf') else minCosts[dst]
        
        로 고쳤더니 메모리가 오히려 늘어났습니다. (15.2MB -> 15.4MB)
        왜 그런지 알 수 있을까요...?
        검색 방법을 알려주셔도 괜찮습니다. 어떻게 찾아봐야할지 감이 전혀 안 잡혀서..
        '''
