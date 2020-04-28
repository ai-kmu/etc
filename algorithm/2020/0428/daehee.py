class Shuttle:                                              # Shuttle 클래스 선언
    def __init__(self, n, t, m, timetable):
        shuttles = range(0, t*n, t)                         # 문제에 제시된 간격 만들기
        self.shuttle = list()
        self.n = n
        self.t = t
        self.m = m
        self.crew = timetable                               # 크루들의 시간표
        
        for idx, shuttle in enumerate(shuttles):            # range로 실제 셔틀 시간표 형식 리스트 생성
            time = (shuttle // 60) *100 + 900
            time += shuttle % 60
            time = str(time).zfill(4)
            self.shuttle.append(time[:2] + ":" + time[2:])
        
    def calc(self):
        shuttle_length = len(self.shuttle)                  # 셔틀 시간표 길이
        crew_length = len(self.crew)                        # 크루 시간표 길이
        
        crew_idx = 0
        fin_shuttle = 0
        for shuttle_idx in range(shuttle_length):           # 셔틀을 0부터 끝까지 탑승시킴
            temp_m = 0
            for i in range(crew_idx, crew_length):          # 크루를 0부터 끝까지 셔틀에 채워나감
                if temp_m == self.m or self.crew[i] > self.shuttle[shuttle_idx]:  # 셔틀이 꽉찬경우 or 셔틀이 이미 지나간 경우
                    fin_shuttle = shuttle_idx + 1
                    if fin_shuttle >= shuttle_length:   # 마지막 셔틀이면 탈 수 있도록 시간을 조절해야함
                        i_minimum = i-1
                        a = self.crew[i_minimum][:3] + str(int(self.crew[i_minimum][3:])-1).zfill(2)
                        if 0 == int(self.crew[i_minimum][3:]):
                            a = str(int(self.crew[i_minimum][:2])-1).zfill(2)+":59"
                        return min(a, self.shuttle[shuttle_idx])   # 탑승한 마지막사람보다 1분 빨리타거나, 마지막 셔틀시간과 동일하게 탑승
                    
                    crew_idx = i
                    break
                temp_m += 1
                if i == crew_length-1 and shuttle_idx == shuttle_length-1 and temp_m == self.m: # 셔틀도 마지막인데 사람도 꽉참(나밖에 못탐)
                    i_minimum = i
                    a = self.crew[i_minimum][:3] + str(int(self.crew[i_minimum][3:])-1).zfill(2)
                    if 0 == int(self.crew[i_minimum][3:]):
                        a = str(int(self.crew[i_minimum][:2])-1).zfill(2)+":59"
                    return min(a, self.shuttle[shuttle_idx])
                
                
        return self.shuttle[fin_shuttle]
                
                
                
def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()  # 오름차순 정렬해서 넣어줌
    a = Shuttle(n, t, m, timetable)
    answer = a.calc()
    return answer
