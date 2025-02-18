class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats = sorted(seats)
        students = sorted(students)
        aws = 0
        for i in range(len(seats)):
            aws += abs(seats[i] - students[i])
        return aws
