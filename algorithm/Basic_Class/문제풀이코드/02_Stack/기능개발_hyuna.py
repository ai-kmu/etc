from collections import deque
def solution(progresses, speeds):
    answer = []
    
    # popleft()를 해주기 위해 deque으로 변환한다
    prog_dq = deque(progresses)
    speed_dq = deque(speeds)
    
    while len(prog_dq):
        # 작업 진도가 100 미만이라면 작업 속도를 더해준다
        for i in range(len(prog_dq)):
            if prog_dq[i] < 100:
                prog_dq[i] += speed_dq[i]
        
        # pop 해줄 횟수를 카운트해줄 변수 n
        n = 0
        # prog_dq의 맨 앞 값이 100보다 작다면 바로 break
        # 맨 앞 값이 100보다 크다면 n이 1 증가. 이후 값도 조회해서 100 미만이 나올 때까지 n을 증가시킨다
        for prog in prog_dq:
            if prog >= 100:
                n += 1
            else:
                break
        
        # n이 나온만큼 prog_dq와 speed_dq를 팝해준다
        for i in range(n):
            prog_dq.popleft()
            speed_dq.popleft()
            
        # n이 0이 아닐 때 append해준다    
        if n:
            answer.append(n)    

    return answer
