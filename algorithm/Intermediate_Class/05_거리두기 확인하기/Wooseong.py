# Brute Force!
def check(place, r, c):
    # 한 칸, L = left, R = right, D = down
    L = place[r][c-1] if c >= 1 else None
    R = place[r][c+1] if c <= 3 else None
    D = place[r+1][c] if r <= 3 else None
    
    # 두 칸, 위와 같은 L/R/D 조합
    RR = place[r][c+2] if c <= 2 else None
    RD = place[r+1][c+1] if r <= 3 and c <= 3 else None
    DD = place[r+2][c] if r <= 2 else None
    DL = place[r+1][c-1] if r <= 3 and c >= 1 else None
    
    # 일단 한 칸 거리에 붙어 있으면 X
    if L == 'P':
        return False
    elif R == 'P':
        return False
    elif D == 'P':
        return False
    
    # 두 칸 거리일 때는 파티션도 없어야 X
    elif RR == 'P' and R != 'X':
        return False
    elif RD == 'P' and (R != 'X' or D != 'X'):
        return False
    elif DD == 'P' and D != 'X':
        return False
    elif DL == 'P' and (D != 'X' or L != 'X'):
        return False
    
    # 그거 아니면 괜찮음
    else:
        return True
    

def solution(places):
    # 정답 리스트
    answer = []
    
    # 각 place 케이스에 대해서
    for place in places:
        # 일단 안 된다고 체크
        temp = 0
        # 문제 생겼을 때 확인 용
        flag = 0
        for r in range(5):
            for c in range(5):
                if place[r][c] == 'P':
                    chk = check(place, r, c)
                    # 하나라도 문제가 생기면 안 됨
                    if not chk:
                        flag = 1
                        break
            # c를 다 못 돌았으면 r을 더 돌 필요가 없음
            else:
                continue
        
        # 문제 생겨서 flag가 꽂히지 않았다면 된다고 바꿈
        if not flag:
            temp = 1                    
        answer.append(temp)
    
    return answer
