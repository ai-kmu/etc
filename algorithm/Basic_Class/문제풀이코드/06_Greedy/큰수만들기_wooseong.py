from collections import deque

def solution(number, k):
    answer = []
    
    # number가 남아 있는 동안
    for num in number:
        # answer의 마지막이 새로운 애보다 작고 (앞에 두 개)
        # 아직 지울 게 남아 있다면 (k)
        while answer and answer[-1] < num and k:
            # 걔 버림
            answer.pop()
            k -= 1
        
        # 새로운 애 넣기
        answer.append(num)
        
    # 테케 12번: number 다 돌았는데 아직 더 지워야한다면
    if k:
        answer = answer[:-k]
        
    return ''.join(answer)
