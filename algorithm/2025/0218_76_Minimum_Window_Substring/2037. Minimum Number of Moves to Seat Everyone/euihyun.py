class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        temp = []
        for i in range(len(seats)):
            temp.append(abs(seats[i] - students[i]))

        
        return sum(temp)
