class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        answer = 0
        seats.sort()
        students.sort()
        for i, j in zip(seats, students):
            answer += abs(i - j)

        return answer
        
