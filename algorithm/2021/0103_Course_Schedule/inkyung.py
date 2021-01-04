class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken_courses = set()
        while prerequisites:
            a, b = prerequisites.pop()
            # 만약 반대의 순서가 있으면 그냥 달성 불가능한 경우
            if [b, a] in prerequisites:
                return False
            for x, y in prerequisites:
                if x == b:
                    if (y, a) in prerequisites:
                        return False
                    else:
                        if (a, b) not in taken_courses:
                            prerequisites.append([a, y])
                            taken_courses.add((a, b))
        return True
