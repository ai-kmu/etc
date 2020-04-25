from collections import deque

def solution(n, t, m, timetable):
    table = []
    for i in timetable:                                    
        a, b = i.split(":")                                    # 시간과 분으로 나눠줌
        table.append(int(a)*100+int(b))                        # 시간을 모두 숫자로 바꿈 10:00 -> 1000
    table.sort()                                               # table 정렬
    table = deque(table)                                       # table을 deque로 바꿔줌

    bus_arr_time = 900                                         # 첫 버스 9시
    crew_in_bus = 0
    while n != 1:                                              # 마지막 버스 전까지
        crew = table.popleft()                                 # crew를 순서대로 불러옴
        if crew <= bus_arr_time:                               # crew가 bus 도착 이전에 왔다면
            crew_in_bus += 1                                   # bus를 탄 crew에 추가
        else:                                                  # bus 도착 이후라면 다음 bus를 타야함 ( sort했기 때문에 뒤에 사람들 모두 같음 )
            table.appendleft(crew)                             # 다시 deque 앞에 넣고
            bus_arr_time = change_time(bus_arr_time, t)        # 다음 bus 시간을 t만큼 더해 바꿔줌 
            n -= 1                                             # 남은 버스 운행 횟수를 1 빼주고
            crew_in_bus = 0                                    # bus 탄 사람을 0으로 바꿔줌
            continue
        if crew_in_bus == m:                                   # bus에 crew가 다 탄 경우도 bus이후에 도착한 crew인 경우와 같이 값들을 초기화해줌
            bus_arr_time = change_time(bus_arr_time, t)
            n -= 1
            crew_in_bus = 0

    for i in range(m-1):                                       # 마지막 bus에 대해 bus에 탈 수 있는 crew의 숫자-1 만큼 실행
        if not table:                                          # 남은 crew가 없다면
            answer = time(bus_arr_time//100, bus_arr_time%100) # bus 도착 시간에 맞춰서 나가면 된다
            return answer

        crew = table.popleft()                                 
        if crew <= bus_arr_time:                               # crew가 bus 도착 전이라면 
            continue                                           # 넘어감
        else:                                                  # bus 도착 후에 온 crew가 남았다면
            answer = time(bus_arr_time//100, bus_arr_time%100) # bus 시간에 맞춰 도착하면 됨
            return answer

    if not table:                                              # 마지막 한자리가 남았다면 
        answer = time(bus_arr_time//100, bus_arr_time%100)     # 마지막 bus 도착시간에 도착하면 됨
    else:
        last_crew = table.popleft()                            # 아직 crew가 남았다면
        if last_crew <= bus_arr_time:                          # crew보다 1분 전에 도착하면 됨
            if last_crew%100 == 0:
                arr_wait = last_crew-100+59
            else:
                arr_wait = last_crew-1
            answer = time(arr_wait//100, arr_wait%100)
        else:
            answer = time(bus_arr_time//100, bus_arr_time%100)
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
