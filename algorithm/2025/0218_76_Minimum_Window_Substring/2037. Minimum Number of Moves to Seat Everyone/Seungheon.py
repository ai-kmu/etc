
class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        
        # greedy 가장 가까운 것부터 배분
        answer = 0
        # 정렬        


        # clear_student_set = set()
        # clear_seat_set = set()     
        answer = 0
        for i, seat in enumerate(seats):
            print(seat,students[i])
            answer += abs(seat-students[i])



        return answer
        

