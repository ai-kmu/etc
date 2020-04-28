def solution(n, t, m, timetable):
    answer = ''
    hour = 9    #초기 버스 시간
    minute = 0    #초기 버스 분
    arridx = 0    #정류장 도착사람 index
    posthour = 0   #이전 버스 시간
    postmin = 0   #이전 버스 분
    strhour = ""   
    strmin = ""
    sortedtime = sorted(timetable)    # timetable을 온 시간 순서대로 sort
    inbus = [[]for busnum in range(n)]  # 각 버스마다 태우는 인원시간대를 갖는 리스트 ( n * ? ) 2차원
    
    
    for busidx in range(n):
        for  ridenum in range(m):
            person = sortedtime[arridx]
            temphour = int(person[0:2])
            tempmin = int(person[3:])
            
            # 정류장에 온 순서대로 인원을 봤을때 해당 버스를 탑승할수 있으면 inbus리스트에 추가하고 다음 인원 체크하고 아니면 다음 버스에서 체크
            if hour > temphour:                                   
                inbus[busidx].append((temphour,tempmin))
                arridx += 1
            elif hour == temphour:
                if minute >= tempmin:
                    inbus[busidx].append((temphour,tempmin))
                    arridx += 1
            else:
                break
            # 모든 인원을 체크했을때 for문 벗어남
            if arridx == len(timetable):
                break;
        posthour = hour
        postmin = minute
        minute += t
        while minute >= 60:
            minute -= 60
            hour += 1
        if arridx == len(timetable):
            break;
    # 마지막 버스 수용량보다 적은 인원이 탔을경우 마지막 버스시간에 도착하면 된다
    if len(inbus[n-1]) < m :
        strhour = str(posthour)
        strmin = str(postmin)
    # 마지막 버스가 꽉 차있을 경우 마지막으로 탄 사람보다 1분 앞서 도착하면 된다
    else:
        outhour = inbus[n-1][m-1][0]
        outmin = inbus[n-1][m-1][1] -1
        if(outmin < 0):
            outmin += 60
            outhour -= 1
        strhour = str(outhour)
        strmin = str(outmin)
    #형태가 시계와 같은 모습으로 하기위해 한자리 수일경우 앞에 0 추가해 준다    
    if len(strhour) == 1 :
        strhour = "0" + strhour
    if len(strmin) == 1 :
        strmin = "0" + strmin
        
    answer = strhour + ":" + strmin
    
    return answer
