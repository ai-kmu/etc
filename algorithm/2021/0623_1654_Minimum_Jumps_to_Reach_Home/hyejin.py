class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden) 
        max_val = max(forbidden | {x}) + a + b # max값 설정해주기 / 연산량 감소를 위함
        if x == 0: # x가 0일때는 0 return
            return 0
        
        answer = 0
        queue = [(0, 0)]
        forbidden.add(0)
        
        while queue: # bfs로 answer번에서 가능한 모든 경우 queue에 넣기
            new_queue = [] # 다음 queue 초기화 (이전 큐와 섞이지 말아야 함)
            for idx, k in queue: # 큐에 있는 원소 모두 검사해서 다음 위치를 계산 => 다음 큐에 넣기
                if idx == x: # x에 도착했을 때
                    return answer 
                
                if idx+a <= max_val and idx+a not in forbidden: # idx+a가 가도될 때
                    new_queue.append((idx+a, 0)) # append
                    forbidden.add(idx+a)
                if k == 0 and 0 <= idx-b and idx-b not in forbidden: # k가 0일 때, positive로 이동한 idx 
                    new_queue.append((idx-b, 1)) # append
            answer += 1 # 다음 순서엔 1번 추가됨
            queue = new_queue # 큐 업데이트
        
        return -1
