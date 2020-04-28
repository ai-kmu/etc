def solution(n, t, m, timetable):
    table = []
    for i in timetable:                                    
        a, b = i.split(":")                                    # 시간과 분으로 나눠줌
        table.append(int(a)*100+int(b))                        # 시간을 모두 숫자로 바꿈 10:00 -> 1000
    table.sort()

    bus_arr_time = 900                                         # 첫 버스 9시
    crew_in_bus = 0
    crew = 0
    for i in range(n):
        for j in range(m):
            if crew > len(table)-1:                            # 이번 버스에 탈 자리가 남앆다는 의미
                break
            if table[crew] <= bus_arr_time:                    # crew가 bus 도착 이전에 왔다면 탑승자 +1, 다음 crew로 넘어감
                crew_in_bus += 1 
                crew += 1
            else:                                              # crew가 bus시간 안에 안왔다면 다음 bus로 넘어감
                if i != n-1:
                    bus_arr_time = change_time(bus_arr_time, t)        
                    crew_in_bus = 0
                break
            if crew_in_bus == m and i != n-1:                  # bus가 꽉 찼고 다음 bus가 있다면 다음 bus 시간으로 넘어감
                bus_arr_time = change_time(bus_arr_time, t)        
                crew_in_bus = 0
 
    if crew == 0 or crew_in_bus < m:                           # bus에 탈 사람이 없거나 마지막 bus에 crew가 다 차지 않았다면 마지막 bus를 타고간다
        answer = time(bus_arr_time//100, bus_arr_time%100)
        return answer

    last_crew = table[crew-1]                                  # 마지막 bus까지 다 crew가 찼다면 마지막 bus의 마지막 crew보다 1분 빨리오면 된다  
    if last_crew%100 == 0:
        arr_wait = last_crew-100+59
    else:
        arr_wait = last_crew-1
    answer = time(arr_wait//100, arr_wait%100)
    return answer


def time(h, min):                                              # 시간을 분과 초로 나누어서 반환해주는 함수 900 -> "09:00"
    answer = ""
    if h < 10:
        answer += "0"+str(h)
    else:
        answer += str(h)
    answer += ":"
    if min < 10:
        answer += "0" + str(min)
    else:
        answer += str(min)
    return answer


def change_time(time, t):                                      # 다음 bus 시간을 더 할때 시간을 계산해주는 함수 
    if (time%100 + t)//60 == 1:
        time = (time//100 + 1)*100 + (time%100+t)%60
    else:
        time += t
    return time
