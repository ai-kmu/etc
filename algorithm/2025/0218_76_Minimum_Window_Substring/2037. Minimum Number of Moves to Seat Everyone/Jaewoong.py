class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # 1,4,5,9
        # 1,2,3,6
        seats = sorted(seats)
        students = sorted(students)
        ans = 0
        for i in range(len(seats)):
            ans += abs(students[i] - seats[i])
        return ans
