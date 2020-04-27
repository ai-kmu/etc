# 18. 프로그래머스 - 셔틀 버스

def solution(n, t, m, timetable):
    answer = ''

    # 분 단위로 통일해서 정렬
    minute_timetable = [int(time[:2]) * 60 + int(time[3:5]) for time in timetable]
    # print('Minute timetable before sorted : ', minute_timetable)

    minute_timetable.sort()
    # print('Minute timetable after sorted : ', minute_timetable)

    # 셔틀버스 탈 수 있는 마지막 시간
    last_time = (60 * 9) + (n - 1) * t

    # 셔틀버스 운영횟수만큼 반복
    for step in range(n):
        # minute_timetable이 한 번에 탈 수 있는 인원보다 적을 경우
        if len(minute_timetable) < m:
            answer = '%02d:%02d' % (last_time // 60, last_time % 60)
            return answer

        # 마지막 순서가 되었을 때
        if step == n - 1:
            # last_time보다 작거나 같은 크루 존재하면
            if minute_timetable[0] <= last_time:
                # 1분 앞선 시간 설정
                last_time = minute_timetable[m-1] - 1
            answer = '%02d:%02d' % (last_time // 60, last_time % 60)
            return answer

        # 위의 조건문 걸리지 않는 경우
        for other in range(m-1, -1, -1):
            # 버스 도착 시간 -> 09:00
            bus_arrive = (60 * 9) + step * t
            if minute_timetable[other] <= bus_arrive:
                del minute_timetable[other]

n_1 = 1
t_1 = 1
m_1 = 5
timetable_1 = ['08:00', '08:01', '08:02', '08:03']

n_2 = 2
t_2 = 10
m_2 = 2
timetable_2 = ['09:10', '09:09', '08:00']

n_3 = 2
t_3 = 1
m_3 = 2
timetable_3 = ['09:00', '09:00', '09:00', '09:00']

n_4 = 1
t_4 = 1
m_4 = 5
timetable_4 = ['00:01', '00:01', '00:01', '00:01', '00:01']

n_5 = 1
t_5 = 1
m_5 = 1
timetable_5 = ['23:59']

n_6 = 10
t_6 = 60
m_6 = 45
timetable_6 = ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59',
               '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59',
               '23:59', '23:59']

print(solution(n_1, t_1, m_1, timetable_1))
print()
print(solution(n_2, t_2, m_2, timetable_2))
print()
print(solution(n_3, t_3, m_3, timetable_3))
print()
print(solution(n_4, t_4, m_4, timetable_4))
print()
print(solution(n_5, t_5, m_5, timetable_5))
print()
print(solution(n_6, t_6, m_6, timetable_6 ))
