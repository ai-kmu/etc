"""
조건은 2가지
    1. 사람수가 꽉차서 못타면 안된다
    2. 막차에는 타야된다.
    
우선 단위가 2개면 다루기 어려우므로 단위를 분으로 통일한다
ex) 09:15  ==>  555
"""

def solution(n, t, m, timetable): # 버스는 n회 t분 간격으로 도착하여 최대 m명의 승객을 태운다.
    """
        lastChance : 버스를 탈 마지막 기회
        bus_times : 버스가 도착하는 시간들 (단위 : 분)
        clues : clue들이 버스에 도착하는 시간들 (단위 : 분)
    """
    lastChance = 539         
    bus_times = [540 + i*t for i in range(n)]     
    clues = sorted([int(clue.split(":")[0]) * 60 + int(clue.split(":")[1]) for clue in timetable])   
    num_clue = len(clues)
    clue_idx = 0                # 현재 회사에 간 clue들의 수
        
    for bus_time in bus_times:                      # 버스가 도착할 때마다
        empty_seat = m
        while empty_seat > 0:                       # 자리에 clue를 태운다
            if clue_idx < num_clue:                 # 아직 회사에 못간 clue가 있다면
                if clues[clue_idx] <= bus_time:     # 현재 버스가 있을 때 보다 이전에 와있던 clue들을 태운다, 이 때 lastChance는 현재의 clue보다 1분 먼저온 것이다
                    lastChance = clues[clue_idx]-1 
                    clue_idx+=1
                    empty_seat-=1
                else:                               #만일 버스에 빈자리가 남아 있다면 현재 버스가 온 시간이 lastChance이다.
                    lastChance = bus_time
                    break
            else:                                   #모든 인원이 회사에 도착했다면 막차시간이 lastchance이다.
                lastChance = bus_times[-1]
                answer = str(lastChance // 60).zfill(2) + ":" + str(lastChance % 60).zfill(2)
                return answer                

    
    answer = str(lastChance // 60).zfill(2) + ":" + str(lastChance % 60).zfill(2)
    return answer
