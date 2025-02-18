class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum([abs(stu - seat) for stu, seat in zip(sorted(students), sorted(seats))])
