from queue import PriorityQueue

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        sort_courses = sorted(courses, key=lambda x : (x[1], x[0]))    # 강의 기간에 따라 정렬
        q = PriorityQueue()                                            # 우선순위 큐를 생성
        q.put((sort_courses[0][0]*(-1), sort_courses[0][1]))
        """
        첫 번째 강의 기간을 큐에 넣기
        -1을 기간에 곱하는 것은 우선순위를 역순으로 하여
        강의 기간이 긴 것의 우선순위를 높여
        강의 기간이 기한보다 커졌을 경우 강의 기간이 가장 긴(우선순위가 높은) 강의부터
        뽑기 위해서
        """
        now_date = sort_courses[0][0]                                  # 현재까지 강의를 들은 기간 저장 
        for (t, d) in sort_courses[1:]:                                # 정렬된 리스트의 2번째부터
            if now_date + t <= d:                                      # 현재까지 강의를 들은 기간과 이번에 들을 기간을 합친 것이 기한보다 짧다면
                q.put((t*(-1), d))                                     # 우선순위 큐에 저장
                now_date += t                                          # 강의를 들은 기간 저장
            else:                                                      # 현재까지 강의를 들은 기가과 이번에 들을 기간을 합친 것이 기한보다 길다면
                q.put((t*(-1), d))                                     # 우선순위 큐에 저장
                now_date += t                                          # 강의를 들은 기간 저장
                now_date += q.get()[0]                                 # 우선순위 큐에서 강의 기간이 가장 긴 강의를 찾아서 강의를 들은 기간에서 빼주기
        return q.qsize()                                               # 우선순위 큐의 크기를 
