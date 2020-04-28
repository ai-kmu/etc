#n : 셔틀 운행 횟수
#t : 셔틀 운행 간격(분)
#m : 한 셔틀에 탈 수 잇는 최대 크루 수
#timetable : 크루가 대기열에 도착하는 시각을 모은 배열

# 0 ＜ n ≦ 10 ( 셔틀 운행 횟수는 n 이하 )
# 0 ＜ t ≦ 60 ( 셔틀 운행 간격은 60분 이하 )
# 0 ＜ m ≦ 45 ( 한 셔틀에 탈 수 있는 최대 크루 수는 45명 이하)

def solution(n, t, m, timetable):

    shuttle_bus = []
    shuttle_bus.append("09:00")
    hour = 9
    min = 0

    # 셔틀이 데리고 가는 마지막 시간 계산
    for i in range(n - 1):  # 운행시간이 9:00부터 시작하니까

        min += t  # 셔틀 운행 간격을 더해줌

        if min >= 60:  # t분이 60분이상이면 시간에 더해줌
            hour += 1
            min = 0
        if hour == 9:  # 9시일 경우
            if min < 10:  # minute이 10분보다 작으면
                time_string = "09:0" + str(min)  # 10분보다 작으니까(한자릿수) 맨 뒤에 붙임
                shuttle_bus.append(time_string)
            else:  # minute이 10분보다 같거나 크면
                time_string = "09:" + str(min)  # 10분보다 같거나 크니까(2자릿수)
                shuttle_bus.append(time_string)
        else:  # 10시 이상일 경우
            if min < 10:  # minute이 10분보다 작으면
                time_string = str(hour) + ":0" + str(min)
            else:  # minute이 10분보다 같거나 크면
                time_string = str(hour) + ":" + str(min)

            shuttle_bus.append(time_string)

    # 오름차순으로 크루가 도착하는 시간 정렬
    timetable.sort()

    # 셔틀 운행 횟수만큼 반복하면서
    for i in range(n):
        # 한 셔틀에 탈 수 있는 크루수보다 총 크루수가 적은 경우
        if len(timetable) < m:
            return shuttle_bus[-1] # 셔틀이 오는 제일 마지막 시간에 타도 상관없으니 마지막 시간에 탑승

        # 한 셔틀에 탈 수 있는 크루수(m)보다 총 크루수가 같거나 많은 경우
        # 현재 셔틀이 마지막 셔틀이면,
        if i == n - 1:
            # 크루중 제일 빨리 타는 사람이  마지막 셔틀 도착 시간보다 늦을 경우
            if timetable[0] > shuttle_bus[i]:
                return shuttle_bus[i] # 마지막 셔틀 도착 시간에 타고가면 됨(어차피 나보다 다 늦으니까)
            # 크루중 제일 빨리 타는 사람이  마지막 셔틀 도착 시간보다 빠를 경우
            hour, min = timetable[m - 1].split(':') #한번 셔틀에 태울때 가장 마지막에 탑승하는 사람의 시간
            hour, min = int(hour), int(min) # 그 시간을 숫자로 변경
            min -= 1  # 크루 중 탑승할 수 있는 마지막 사람보다는 빨리 타야되니까, #여기서 hour,minute이 내가 탑승해야하는 시간

            #내가 탑승해야하는 시간을 "??:??"형식으로 바꿔주기
            #만약에 해당 분이 -1분이라면, (09:00~ 08:59분이 되는 경우의 변환 )
            if min == -1:
                #59분으로 변경
                min = 59
                #시간은 1시간 줄임
                hour -= 1

            # 만약에 해당 시간이 10시 미만이면
            if hour < 10:
                # 만약에 해당 분이 10분 미만이면
                if min < 10:
                    return "0" + str(hour) + ":0" + str(min)
                # 만약에 해당 분이 10분 이상이면
                else:
                    return "0" + str(hour) + ":" + str(min)
            # 만약에 해당 시간이 10시 이상이면
            else:
                # 만약에 해당 분이 10분 미만이면
                if min < 10:
                    return str(hour) + ":0" + str(min)
                # 만약에 해당 분이 10분 이상이면
                else:
                    return str(hour) + ":" + str(min)

        # 현재 셔틀이 마지막 셔틀이 아니라면,
        for j in range(m - 1, -1, -1): # 한 셔틀에 탈 수 있는 최대 크루 수 만큼 반복하면서
            if timetable[j] <= shuttle_bus[i]: # 지금 셔틀 시간보다 크루가 기다리러 온 시간이 작으면
                timetable.pop(j) # 크루를 없애줌( 셔틀 탄 거니까 )