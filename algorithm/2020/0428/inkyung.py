def solution(n, t, m, timetable):
    """
    정답률 58.3
    """
    answer = ''
    timetable.sort()
    
    #bus_table에 기준 시간인 09:00와 버스를 탈 수 있는 마지막 시간을 넣어줌
    bus_table = ['09:00']
    hour, minute = 9, 0
    for i in range(n-1):
        minute += t
        if minute >= 60:
            hour += 1
            minute = 0
    if minute >= 10:
        if hour < 10:
            time = '0' + str(hour) +':' + str(minute)
        else:
            time = str(hour) + ':' + str(minute)
    else:
        if hour < 10:
            time = '0' + str(hour) + ':0' + str(minute)
        else:
            time = str(hour) + ':0' + str(minute)
    
    #만약 마지막에 줄 선 사람이 9시 이후에 줄을 선다면 bus_table에 마지막 
    #버스를 탈 수 있는 시간을 넣어줌
    if int(timetable[-1][:2]) >= int(bus_table[0][:2]) and time != '09:00':
        bus_table.append(time)
    bus_table.sort()
    
    print(bus_table)

    
    person_num = n * m  #셔틀을 타고 이동할 수 있는 총 인원
    
    #만약 마지막에 줄을 선 사람이 23:59에 줄을 섰고 탈 수 있는 인원과 이미 줄을 선 사람의
    #숫자가 같다면 콘은 그다음날 탄다
    if timetable[-1] == '23:59' and person_num == len(timetable):
        return '09:00'
    
    for time in range(n):
        #한번에 탈 수 있는 자리가 기다리는 사람보다 더 많다면 제일 늦게와서 타면 됨
        if len(timetable) < m :
            return bus_table[-1]
        
        #총 셔틀로 이동할 수 있는 인원보다 기다리는 사람이 적을 때는 
        #제일 마지막 버스직전에 오면 됨
        if len(timetable) < person_num:
            temp = bus_table[-1].split(':')
            hour, minute = int(temp[0]), int(temp[1])
            minute -= 1
            if minute == -1:
                hour -= 1
                minute = 59
            
            if hour < 10 and minute < 10:
                return '0' + str(hour) + ':0' + str(minute)
            elif hour < 10 and minute > 10:
                return '0' + str(hour) + ':' + str(minute)
            elif hour > 10 and minute < 10:
                return str(hour) + ':0' + str(minute)
            else:
                return str(hour) + ':' + str(minute)
        
        if len(timetable) == person_num:
            temp = timetable[-1].split(':')
            hour, minute = int(temp[0]), int(temp[1])
            minute -= 1
            
            if minute == -1:
                hour -= 1
                minute = 59
            
            if hour < 10 and minute < 10:
                return '0' + str(hour) + ':0' + str(minute)
            elif hour < 10 and minute > 10:
                return '0' + str(hour) + ':' + str(minute)
            elif hour > 10 and minute < 10:
                return str(hour) + ':0' + str(minute)
            else:
                return str(hour) + ':' + str(minute)
