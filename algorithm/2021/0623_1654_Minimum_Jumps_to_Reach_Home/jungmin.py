class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        queue=collections.deque() # (위치, 뒤로 가는 step 수)을 저장하는 queue 선언
        queue.appendleft([0,0])
        c=0 # h는 점프 횟수
        visit=set() # 방문했던 위치를 저장하기 위해 집합 선언
        visit.add(0) # 처음에는 0에서 시작
        
        # 2번 연속으로 뒤로 갈 수 없으므로 a와 b의 크기에 따라서 수평에서의 최대로 갈 수 있는 위치 한계를 저장
        limit=x+b if a>b else max(x,max(forbidden))+2*b
            
        while(len(queue)>0):
            for i in range(len(queue)):
                current=queue.pop()
                if current[0]==x: # 현재 위치가 집의 위치랑 같은 경우 카운트 횟수 c 출력
                    return c
                forward, backward = current[0]+a, current[0]-b # 현재 위치에서 앞으로 a 점프할 때 위치, 뒤로 b 점프할 때 위치 두개 저장
            # 만약 뒤로 갔을 때 그 위치가 0이상이고 방문한 적이 없으며 이전 단계에서 bakward 한적 없고 문제 조건을 만족하면 queue에 저장
                if backward>=0 and backward not in forbidden and backward not in visit and backward<=limit and current[1]<1:
                    queue.appendleft([backward, current[1]+1])
                    visit.add(backward)
                # 앞으로 갔을 때 그 위치가 0이상이고 방문한 적이 없으며 문제 조건을 만족하는 경우 queue에 저장
                if forward>=0 and forward not in forbidden and forward not in visit and forward<=limit:
                    queue.appendleft([forward,0])
                    visit.add(forward)
            c+=1 # 이전 단계에서의 queue의 길이만큼 for문 다 돌았으면 점프 횟수 카운트
        return -1
