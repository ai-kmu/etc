from collections import deque

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 의자 정렬 후 deque -> 하나 씩 꺼내 쓰기 위함
        seats.sort()
        seats = deque(seats)

        # 학생 정렬하고 탐색
        students.sort()
        answer = 0
        for s in students:
            # 가장 가까운, 즉 가장 왼쪽의 의자 꺼내서
            curr_seat = seats.popleft()
            # 그 의자에 앉기
            answer += abs(curr_seat - s)

        return answer
