# BFS

class Solution(object):
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        # 딕셔너리에서 key는 시작 노드, value는 목적지와 price 쌍으로 구성
        graph=collections.defaultdict(dict)
        for u, v, w in flights:
            graph[u][v]=w
       
        queue = collections.deque([(src,0)]) # 비행 경로를 저장할 큐 생성(src에서 시작)
        ans, step = float('inf'), 0 # 일단 비용 저장할 ans 무한대로 초기화, 첫 스탭 0
        
        while queue:
            for _ in range(len(queue)):
                cur,cost = queue.popleft() # 현재 노드랑 그때의 비용을 하나씩 뽑아와서
                if cur == dst: # 현재 노드가 목적지인 경우
                    ans=min(ans,cost) # 더 작은 비용 찾아 비용 업데이트
                    continue
                # 그렇지 않은 경우 다음 정류장과 비용을 찾는다
                for v,w in graph[cur].items():
                    if cost + w > ans: # 만약 새 경로가 기존 경로보다 크면 넘어가고
                        continue
                    queue.append((v,cost+w)) # 더 좋은 경로이면 큐 경로에 추가
            if step > K: break # k개 경유지 이내로 도착해야하니까 넘어가면 break
                
            step+=1
        return -1 if ans == float('inf') else ans # 경로가 존재하지 않을 땐 -1 리턴, ans 리턴
