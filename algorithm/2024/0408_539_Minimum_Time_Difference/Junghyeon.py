# 시간을 분 단위로 바꿔서 정렬하고 인접 리스트 간의 최소 차이를 저장 
# 가장 큰 수와 작은 수의 차이도 추가적으로 계산해야함
# 저번 코테 문제에서 조금 쉬운 버전...?

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_list = []
        min_time = 9999

        # 입력을 정수의 분 형식으로 변환
        for i in timePoints:
            h = int(i.split(":")[0])
            m = int(i.split(":")[1])
            
            time_list.append(60*h + m)
            
        time_list.sort()

        
        for i in range(len(time_list)-1):
            # 최솟값 업데이트
            min_time = min(time_list[i+1]-time_list[i], min_time)
        
        # 마지막 케이스 : 1440(24시의 분)에서 가장 큰 값을 빼고 가장 작은 값을 더하면 두 수의 차이가 됨 
        tmp_time = 1440 - time_list[-1] + time_list[0]
        min_time = min(tmp_time, min_time)

        return min_time
