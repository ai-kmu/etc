class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(students)
        seat_idx, student_idx = 0, 0
        print(seats, students)
        pair = []
        while 1:
            if seat_idx == n or student_idx == n:
                break
            if seats[seat_idx] == students[student_idx]:
                pair.append((seat_idx,student_idx))
                student_idx += 1
                seat_idx += 1
            elif seats[seat_idx] > students[student_idx]:
                student_idx += 1
            else:
                seat_idx += 1
        if pair: # 중복 제거
            idx = 0
            for s, st in pair:
                del seats[s-idx]
                del students[st-idx]
                idx += 1
        ans = 0
        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])
        return ans
