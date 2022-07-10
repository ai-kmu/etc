# 오답
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer = []
        prereq = {}
        goal = {}

        for subject in prerequisites:
            if subject[1] not in prereq:
                prereq[subject[1]] = 1
            else:
                prereq[subject[1]] += 1
            # print(prereq)
            if subject[0] not in goal:
                goal[subject[0]] = 1
                # print(goal)
            else:
                goal[subject[0]] += 1

        while prereq:
            answer.append(max(prereq.keys()))

            prereq.pop(max(prereq))
 
        while goal:

            if max(goal) in answer:
                goal.pop(max(goal))
            else:
                answer.append(goal.pop(max(goal)))

        return answer
