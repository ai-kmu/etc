def solution(n, t, m, timetable):
    answer = ''
    #timetable 분으로 환산 후 순서대로 정렬하기
    timetable = [int(time[:2])*60 + int(time[3:5]) for time in timetable]
    timetable.sort()

    total = len(timetable) #태워야 할 총 인원 수
    shuttle = 0 #셔틀버스에 탄 인원 수
    last_bus = 0 #마지막 버스 시간
    last_bus = 540 + (n-1)*t #마지막 버스 시간(분으로 환산)

    for i in range(n):
        bus_time = 540 + t * i #버스 출발 시각
        if total < m: #인원 수가 적다면 마지막 버스 시간으로 설정
            answer = '%02d:%02d' %(last_bus // 60, last_bus % 60)
            break
        
        while True:
            if timetable[0] <= bus_time:
                shuttle += 1 #버스 시각보다 일찍 온 사람들 한 명씩 태우기
                if shuttle == m:
                    break
                if len(timetable) == 0:
                    break
                if len(timetable) == 1:
                    del timetable[0]
                    break
                del timetable[0]
            else:
                break
            
        if i == n-1: #마지막 버스일 때
            if shuttle == m:
                timetable[0] -= 1
                answer = '%02d:%02d' %(timetable[0] // 60, timetable[0] % 60)
                break
            else:
                answer = '%02d:%02d' %(bus_time // 60, bus_time % 60)
                break
        else:
            if len(timetable) == 0: #마지막 버스가 아닌데 대기열이 없다면
                answer = '%02d:%02d' %(last_bus // 60, last_bus % 60)
                break
            if shuttle == m:
                del timetable[0]
            shuttle = 0 #버스 인원 초기화
    return answer
