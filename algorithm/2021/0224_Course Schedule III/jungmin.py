class Solution(object):
    def scheduleCourse(self, courses):
        if courses == 0 or len(courses) == 0:
            return 0

        day_sort = sorted(courses, key = lambda x : x[1]) # d값 기준으로 course 리스트 정렬

        during = 0
        count = 0

        for i in range(len(day_sort)):

            during = during + day_sort[i][0] # 처음 0부터 코스에 들어갈 때마다 t값을 누적해서 더한다.

            if during <= day_sort[i][1]:
                count+=1 # 만약에 다음 course를 수행할 수 있으면 카운트한다.
                if i == len(day_sort)-1:
                    return count # 만약에 courses를 다 수행했다면 courses 길이값 출력

            elif during > day_sort[i][1]:
                return count # 만약 더이상 course를 수행할 수 없으면 코스 수행한 만큼 count 출력
