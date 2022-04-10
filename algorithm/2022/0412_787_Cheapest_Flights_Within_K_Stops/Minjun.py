import copy

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # 참고용 배열 만들기
        prev = [float("inf")] * n
        
        # 스타팅 포인트 지정
        prev[src] = 0
        
        
        for i in range(1, k+2):
            # 비교용
            now = copy.deepcopy(prev)
            
            # 플래그
            changed = False
            
            for flight in flights:
                
                # src
                start = flight[0]
                # dst
                dest = flight[1]
                # cost
                cost = flight[2]
                
                if prev[start] != float("inf") and prev[start]+ cost < now[dest]:
                    
                    now[dest] = prev[start] + cost
                    changed = True
            
            # 갱신 실패하면 멈춘다
            if not changed:
                break
            
            # 계산한 값 옮겨 담기
            prev = copy.deepcopy(now)
        
        ans = 0
        
        # 갱신 성공 - 가능했던 루트면 반환
        if prev[dst] != float("inf"):
            ans = prev[dst]
        
        # inf면 불가능 루트 -1 반환
        else:
            ans = -1
            
        return ans
