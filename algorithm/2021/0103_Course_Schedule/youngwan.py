class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        rule = [[] for i in range(numCourses)]        
        for pre in prerequisites:
            rule[pre[0]].append(pre[1])                 # 미리 들어야 하는 course를 체크 -> [0,1]인 경우 0을 듣기 위해선 1을 들어야 한다
                                                        # 따라서 0번에 1번 수업을 넣고 1보다 먼저 0번 수업을 들은 경우에는 False를 반환
        
        listened = [0] * numCourses                     # 문제 없이 수강한 과목은 1, 수강하지 않은 과목은 0, 올바르게 수강했는지 체크 중인 과목은 -1
        
        for num in range(numCourses):
            if listened[num] == 1:                      # 올바르게 수강한 과목인 경우 넘어감
                continue
            schedule = [num]                            
            while schedule:
                listen = schedule[-1]
                if listened[listen] == 1:               # 올바르게 수강했다고 체크된 수업은 stack에서 빼고 넘어감
                    schedule.pop()
                    continue
                if listened[listen] == 0:               # 아직 수강하지 않은 과목인 경우
                    listened[listen] = -1               # 체크 중인 상태로 바꾸고
                    for havelisten in rule[listen]:     # 이 강의를 위해 미리 들어야 하는 강의들을 체크
                        if listened[havelisten] == -1:  # 만약 이 강의 다음으로 들어야 할 강의(havelisten)를 미리 들었다면 
                            return False                # False 반환
                        elif listened[havelisten] == 0: # 아직 듣지 않았다면
                            schedule.append(havelisten) # stack에 추가
                
                elif listened[listen] == -1:            # 체크가 끝난 경우에는
                    schedule.pop()                      # stack에서 빼고
                    listened[listen] = 1                # 수강한 강의로 바꾸어준다
            
        return True
