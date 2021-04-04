import heapq
from collections import defaultdict

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        
        full = set() # 비 왔던 호수 저장하기 위한 set 생성
        output = [] # 최종 출력 리스트 생성
        step_info = defaultdict(list) # 호수 번호별 비가 온 때를 저장하기 위한 defaultdict 선언
        future = [] # 미래에 어떤 호수가 또 비가 올 것인지 따로 저장
        
        for i in range(len(rains)):
            step_info[rains[i]].append(i) # 호수 번호별 비가 온 때(rains index)를 저장
        
        for i in range(len(rains)):
            if rains[i] > 0: # 비가 어느 호수에 왔을 경우
                if rains[i] in full: # 만약에 물이 차있던 호수에 비가 또 오면
                    return [] # 그 country는 홍수가 난 것이므로 빈 리스트를 return
                
                full.add(rains[i]) # 비가 온 홍수 번호를 full에 저장
                
                
                step_info[rains[i]].pop(0) # step_info에서 현재 호수의 index 제거
                if step_info[rains[i]]: # 만약 현재 index를 제거해도 다른 index값이 남아 있으면
                    heapq.heappush(future, step_info[rains[i]][0]) # 그 index를 future에 저장
                    
                output.append(-1) # 비가 왔으므로 output에 -1 저장
                
                
            elif rains[i] == 0: # 비가 안올 경우
                if future: # future에 값이 존재하면
                    next_idx = heapq.heappop(future) # future안 하나의 값을 다음 인덱스로 저장해서
                    output.append(rains[next_idx]) # rains의 해당 인덱스에 해당한 값을 출력에 추가
                    full.remove(rains[next_idx]) # 채워진 물을 비웠으므로 full에서 제거
                    
                else:
                    output.append(1) # 미래에 비올 호수가 없으면 출력에 1 추가
                    
                
        return output
